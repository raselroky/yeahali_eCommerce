from rest_framework import serializers
from .models import Role_And_Permission,Action,Update_Message
from django.contrib.auth.models import Group, Permission,User
from django.contrib.auth.hashers import make_password

class Role_And_Permission_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Role_And_Permission
        fields=('__all__')

class Action_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Action
        fields=('__all__')

class Permission_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Permission
        fields=('id','name')
        #depth=0

class Update_Message_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Update_Message
        fields=('__all__')

class User_Serializer(serializers.ModelSerializer):
    
    #confirmed_password=serializers.CharField(style={'input_type':'password'},write_only=True)
    class Meta:
        model=User
        fields=('id','username','email','password')
        extra_kwargs={
            'password':{'write_only':True}
        }
    
    def create(self,validated_data):
        password=validated_data.pop('password',None)
        instance=self.Meta.model(**validated_data)

        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance