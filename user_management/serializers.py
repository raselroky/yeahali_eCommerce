from rest_framework import serializers
from .models import Registration_All
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from phonenumber_field.serializerfields import PhoneNumberField

class Registration_All_Serializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    confirm_password = serializers.CharField(write_only=True, required=True)
    

    class Meta:
        model=Registration_All
        fields=('id','first_name','last_name','email','country','address','mobile','gender','marital_status','date_of_joining','role','image','password','confirm_password')
        extra_kwargs = {
            'password': {'write_only': True},
            'confirm_password': {'write_only': True},
        }
    
    def validate(self, data):
        if data.get('password') != data.get('confirm_password'):
            raise serializers.ValidationError("Passwords do not match.")
        return data

    def create(self, validated_data):
        confirm_password = validated_data.pop('confirm_password', None)
        instance = super().create(validated_data)
        instance.set_password(validated_data['password'])
        instance.save()
        return instance

    def update(self, instance, validated_data):
        confirm_password = validated_data.pop('confirm_password', None)
        instance = super().update(instance, validated_data)

        if 'password' in validated_data and validated_data['password']:
            instance.set_password(validated_data['password'])
            instance.save()

        return instance