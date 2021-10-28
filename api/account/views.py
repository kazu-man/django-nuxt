from rest_framework import viewsets, generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ItemSerializer
from .serializers import ItemListSerializer
from .serializers import CategorySerializer
from .serializers import UserSerializer
from .serializers import UserRegistrationSerializer
from .models import Item
from .models import Category
from .models import User
import json
from django_filters import rest_framework as filters
from rest_framework.permissions import IsAuthenticated
from django.db.models import Count, Sum
from datetime import datetime as dt
from account.view_modules.module import module
import inspect
from rest_framework.decorators import (api_view, permission_classes, list_route)
from rest_framework.permissions import AllowAny


class UserListView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request):

        # Validating our serializer from the UserRegistrationSerializer
        serializer = UserRegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Everything's valid, so send it to the UserSerializer
        model_serializer = UserSerializer(data=serializer.data)
        model_serializer.is_valid(raise_exception=True)
        model_serializer.save()

        return Response(model_serializer.data)

# item検索用のフィルター
class CustomFilter(filters.FilterSet):
    # フィルタの定義
    price_gte = filters.NumberFilter(field_name='price', lookup_expr='gte')
    price_lte = filters.NumberFilter(field_name='price', lookup_expr='lte')
    purchase_date = filters.DateFromToRangeFilter(field_name='purchase_date')
    purchase_date_time = filters.DateTimeFromToRangeFilter(field_name='purchase_date')

    class Meta:
        model = Item
        fields = ['price','purchase_date'] #定義したフィルタを列挙

    @property
    def qs(self):
        parent = super(CustomFilter, self).qs
        user = self.request.user  
        if user.is_authenticated:
            print("login user :",user)
            return parent.filter(user_id=user.id) 
        print("no login !!!")
        return parent.filter(user_id=-1)


class ItemViewSet(viewsets.ModelViewSet):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()
    #フィルターの設定
    filter_backends = [filters.DjangoFilterBackend]
    filter_class = CustomFilter

    # 複数item同時作成用のデコレータ
    def multi_create(serializer_class=None):
        def __multi_create(function):
            def __wrapper(self, request, *args, **kwargs):
                many = False
                if isinstance(request.data, list):
                    many = True
                print(type(request.data))
                serializer = serializer_class(data=request.data, many=many, context={'request': request})
                if serializer.is_valid():
                    serializer.save()
                    headers = self.get_success_headers(serializer.data)
                    data = serializer.data
                    result = function(self, request, *args, **kwargs)
                    if result is not None:
                        return result
                    if many:
                        data = list(data)
                    return Response(data,
                                    status=status.HTTP_201_CREATED,
                                    headers=headers)
                else:
                    print("INVALID!!!")
                    print(serializer.errors)
                    return Response(serializer.errors,
                                    status=status.HTTP_400_BAD_REQUEST)
            return __wrapper
        return __multi_create

    @multi_create(serializer_class=ItemSerializer)
    def create(self, request):
        pass


# 複数itemの同時更新用のviewSet
class ItemListViewSet(viewsets.ModelViewSet):
    serializer_class = ItemListSerializer
    queryset = Item.objects.all()

    def put(self, request, *args, **kwargs):
        items = Item.objects.all()
        serializer = ItemListSerializer(items, child=ItemSerializer(),data=request.data)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data,status.HTTP_201_CREATED)


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    # permission_classes = (IsAuthenticated,)


# itemの合計金額取得用のviewSet
class TotalView(APIView):
    # permission_classes = [IsAuthenticated]

    def post(self, request,test, *args, **kwargs):

        date = request.data
        allList =  Item.objects.filter().all()
        total = 0
        for item in allList:
            total += int(item.price)

        return Response(total,status.HTTP_201_CREATED)

    # def get(self, *args, **kwargs):
    def get(self, request,date, *args, **kwargs):

        allList =  Item.objects.filter(purchase_date__range=[date, date],user_id=request.user.id)

        total = 0
        for item in allList:
            total += int(item.price)

        return Response(total,status.HTTP_201_CREATED)


# itemの月毎の剛家金額/リスト取得用のviewSet
class TotalMonthView(APIView):

    # def get(self, *args, **kwargs):
    def get(self, request,fromDate,toDate, *args, **kwargs):
        
        result = {};
        allList =  Item.objects.filter(purchase_date__range=[fromDate, toDate],user_id=request.user.id)

        total = 0
        for item in allList:
            total += int(item.price)

        totalPriceDate = allList.values('purchase_date').annotate(total=Sum('price')).order_by('purchase_date')
        serializedItems = ItemSerializer(allList, many=True)
        totalPriceDate = module.getMonthChartData(totalPriceDate,serializedItems)

        result["total"] = total
        result["totalPriceDate"] = totalPriceDate

        return Response(result,status.HTTP_201_CREATED)


# itemの日毎の剛家金額/リスト取得用のviewSet
class ItemsDateView(APIView):

    # def get(self, *args, **kwargs):
    def get(self, request,fromDate,toDate, *args, **kwargs):

        items =  Item.objects.filter(purchase_date__range=[fromDate, toDate],user_id=request.user.id)
        totalPriceDate = items.values('purchase_date').annotate(total=Sum('price')).order_by('purchase_date')
        serializedItems = ItemSerializer(items, many=True)

        totalPriceDate = module.getChartData(totalPriceDate,serializedItems)

        return Response(totalPriceDate,status.HTTP_201_CREATED)

# 練習用のviewSet
class TestView(APIView):
    serializer_class = CategorySerializer
    def get(self, request, *args, **kwargs):
        """
        Return a list of all users.
        """
        cateName =  Category.objects.all()
        serializer = CategorySerializer(cateName, many=True)

        print(serializer.data)
        # return Response(cateName)
        return Response(serializer.data,status.HTTP_201_CREATED)
    


