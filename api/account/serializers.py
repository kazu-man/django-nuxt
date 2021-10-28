from rest_framework import serializers
from rest_framework.serializers import PrimaryKeyRelatedField
from .models import Category
from .models import Item
from .models import User
import json
from drf_writable_nested import WritableNestedModelSerializer
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('email', 'username','password','is_staff','is_active')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data, *args, **kwargs):

        validated_data['password'] = make_password(
                validated_data.pop('password')
            )
        validated_data['is_active'] = 1
        instance = User.objects.create(**validated_data)

        return instance

# passwordとconfirm_passwordが一致しているか確認する
class UserRegistrationSerializer(serializers.Serializer):
    email = serializers.EmailField()
    username = serializers.CharField(required=False)
    password = serializers.CharField()
    confirm_password = serializers.CharField()

    # def validate_email(self, email):
    #     existing = User.objects.filter(email=email).first()
    #     if existing:
    #         raise serializers.ValidationError("Someone with that email "
    #             "address has already registered. Was it you?")
    #     return email

    def validate(self, data):
        if not data.get('password') or not data.get('confirm_password'):
            raise serializers.ValidationError("Please enter a password and "
                "confirm it.")
        if data.get('password') != data.get('confirm_password'):
            raise serializers.ValidationError("Those passwords don't match.")
        return data



class CategorySerializer(serializers.ModelSerializer):

    # items = ItemSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = "__all__"
        read_only_fields = ('id','items')
        extra_kwargs = {
            "name": {
                "error_messages": {"required": "Give yourself a username"}
            },
            "color": {
                "error_messages": {"required": "Give yourself a color"}
            }
        }

    def __init__(self, *args, **kwargs):
        super(CategorySerializer, self).__init__(*args, **kwargs)


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
        )


    def create(self, validated_data):

        print("CREAT ITEM!!")
        categories = validated_data.get('category_id', None)
        print(validated_data)
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
                ret.append(self.child.update(item, data))

        return ret