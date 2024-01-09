from rest_framework import serializers
from .models import Add_Product,Image_Upload

class Image_Upload_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Image_Upload
        fields=('__all__')


class Add_Product_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Add_Product
        fields=('__all__')


class Add_Product_Show_All_Serializer(serializers.ModelSerializer):
    #product_image = Image_Upload_Serializer(many=True)
    class Meta:
        model=Add_Product
        fields=('__all__')
        depth=3
        
