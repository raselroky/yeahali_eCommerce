from rest_framework import serializers
from .models import Brand,Category,SubCategory

class Brand_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Brand
        fields=('__all__')


class Category_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields=('__all__')
class Category_Show_All_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields=('__all__')
        depth=1


class SubCategory_Serializer(serializers.ModelSerializer):
    class Meta:
        model=SubCategory
        fields=('__all__')
class SubCategory_Show_All_Serializer(serializers.ModelSerializer):
    class Meta:
        model=SubCategory
        fields=('__all__')
        depth=2