from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import ItemViewSet
from .views import CategoryViewSet
from .views import TestView
from .views import TotalView
from .views import TotalMonthView
from .views import ItemsDateView
from .views import ItemListViewSet
from .views import UserListView

from rest_framework_simplejwt import views as jwt_views

router = DefaultRouter()
router.register(r"item", ItemViewSet)
router.register(r"category", CategoryViewSet)
router.register(r"itemList", ItemListViewSet)
router.register(r"userList", UserListView)

 
urlpatterns = [
    path("", include(router.urls)),
    path('total_month/<str:fromDate>/<str:toDate>/', views.TotalMonthView.as_view()),
    path('item_data/<str:fromDate>/<str:toDate>/', views.ItemsDateView.as_view()),
    path('total/<str:date>/', views.TotalView.as_view()),
    path('total/', views.TotalView.as_view()),
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/', include('djoser.urls.jwt'))

    
]