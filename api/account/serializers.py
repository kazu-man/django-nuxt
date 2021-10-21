from rest_framework import serializers
from rest_framework.serializers import PrimaryKeyRelatedField
from .models import Category
from .models import Item
from .models import User
import json
from drf_writable_nested import WritableNestedModelSerializer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'username')

class CategorySerializer(serializers.ModelSerializer):

    # items = ItemSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        # fields = (
        #     "id",
        #     # "name",
        #     # "color",
        #     # "items",
        #     # "created_at"
        # )
        fields = "__all__"

        read_only_fields = ('id','items')

    # def update(self, instance, validated_data):

    #     instance.name = validated_data.get('name', instance.name)
    #     instance.color = validated_data.get('color', instance.color)
    #     instance.save()

    #     return instance


class ItemSerializer(serializers.ModelSerializer):

    categories = CategorySerializer(many=True, read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), write_only=True, required=False)
    user_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(),  required=False)
    id = serializers.IntegerField(required=False)
    class Meta:
        model = Item
        fields = (
            "id",
            "name",
            "price",
            "purchase_date",
            "memo",
            "categories",
            "category_id",
            "user_id"
            # "created_at"
        )
        # fields = "__all__"
        # categories = PrimaryKeyRelatedField(queryset=Category.objects.all())

        # depth = 1

        # extra_kwargs = {
        #     'categories': {'validators': []},
        # }
        # extra_kwargs = {'categories': {'read_only': False}}
        # read_only_fields = ('id',)


    def create(self, validated_data):

        print("CREAT ITEM!!")
        categories = validated_data.get('category_id', None)

        del validated_data['category_id']

        validated_data["user_id"] = self.context['request'].user.id
        instance = Item.objects.create(**validated_data)

        instance.categories.add(categories)
        return instance

    # ManyToManyリレーションに対応するようにオーバーライド
    def update(self, instance, validated_data):
        # request = self.context['request']
        print("UPDATE ITEM!!")
        # print(validated_data.get('name', instance.name))
        categories = validated_data.get('category_id', None)

        del validated_data['category_id']
        # del validated_data['categories']
        categoryList = [categories]
        instance.categories.set(categoryList)
        instance.name = validated_data.get('name', instance.name)
        instance.price = validated_data.get('price', instance.price)
        instance.purchase_date = validated_data.get('purchase_date', instance.purchase_date)
        instance.memo = validated_data.get('memo', instance.memo)
        instance.save()
        return instance

        # print(self)
        # categories = self.data.get('categories')
        # print(validated_data)
        # try:
        #     categories = json.loads(request.data.get('categories', []))
        # except:
        #     categories = request.data.get('categories', [])

        # # categories = validated_data.pop('categories')
        # instance = super(ItemSerializer, self).create(validated_data)
        # # for product in categories:
        # #     InvoiceDetail.objects.create(invoice=invoice, product=product)

        # for category_data in categories:

        #     category = Category.objects.filter(id=category_data['id']).first()
        #     if category is None:
        #         category = Category.objects.create(**category_data)
        #     instance.categories.add(category)
        # return Item.objects.create(**validated_data)



    # def update(self, instance, validated_data):
    #     # print(validated_data)
    #     request = self.context['request']
    #     print("kokomadekitayo!!!")
    #     try:
    #         categories = json.loads(request.data.get('categories', []))
    #     except:
    #         categories = request.data.get('categories', [])

    #     instance.name = validated_data.get('name', instance.name)
    #     instance.price = validated_data.get('price', instance.price)
    #     instance.purchase_date = validated_data.get('purchase_date', instance.purchase_date)
    #     instance.memo = validated_data.get('memo', instance.memo)

    #     instance.categories.clear() 
    #     # categories_dataからcategoriesを追加
    #     for category_data in categories:

    #         category = Category.objects.filter(id=category_data['id']).first()
    #         if category is None:
    #             category = Category.objects.create(**category_data)
    #         instance.categories.add(category)
    #     instance.save()

    #     return instance

# 複数itemの同時作成
class ItemListSerializer(serializers.ListSerializer):
    child = ItemSerializer()

    def update(self, instance, validated_data):
        # Maps for id->instance and id->data item.
        print("UPDATE ITEMS START!!!!")
        item_mapping = {item.id: item for item in instance}
        data_mapping = {item['id']: item for item in validated_data}
        # Perform creations and updates.
        ret = []
        for id, data in data_mapping.items():
            item = item_mapping.get(id, None)
            if item is not None:
                if "category_id" not in data:
                    continue
                # ret.append(self.child.create(data))
            # else:
                ret.append(self.child.update(item, data))

        # Perform deletions.
        # for id, item in item_mapping.items():
        #     if id not in data_mapping:
        #         item.delete()
        return ret