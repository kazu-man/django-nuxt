from django.contrib import admin
from .models import Category
from .models import Item
from .models import UserInfo
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    model = User
# Register your models here.
admin.site.register(Category)  # 追加
admin.site.register(Item)  # 追加
admin.site.register(UserInfo)  # 追加
admin.site.register(User, CustomUserAdmin)
