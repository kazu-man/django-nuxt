from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass

class Category(models.Model):

    class Meta:
        db_table = 'category'

    name = models.CharField(max_length=120, verbose_name="カテゴリー名")
    color = models.CharField(max_length=120, verbose_name="カラー")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str_(self):
        return self.name

class Item(models.Model):

    class Meta:
        db_table = 'item'
        
    name = models.CharField(max_length=120, verbose_name="商品名前")
    price = models.CharField(max_length=120, verbose_name="値段")
    purchase_date = models.DateField(verbose_name="購入日")
    memo = models.TextField(verbose_name="メモ",blank=True)
    categories = models.ManyToManyField(Category, verbose_name="商品", related_name='items')
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str_(self):
        return self.name

