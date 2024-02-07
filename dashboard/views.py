from django.shortcuts import render
from rest_framework import generics,status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from rest_framework import filters
from .models import Role_And_Permission,Action,Update_Message
from .serializers import Role_And_Permission_Serializer,Action_Serializer,Permission_Serializer,Update_Message_Serializer,User_Serializer
from django.contrib.auth.models import Group, Permission,User
from django.contrib.auth import get_user_model
from user_management.models import Registration_All
from user_management.serializers import Registration_All_Serializer,Registration_All_Show_Serializer
from user_management.models import Blacklisted
from user_management.serializers import Blacklisted_Serializer
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import AuthenticationFailed


class Role_And_Permission_Api_Detail(APIView):
    def get_object(self,pk):
        try:
            return Role_And_Permission.objects.get(id=pk)
        except Role_And_Permission.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = Role_And_Permission_Serializer(snippet)
        return Response(serializer.data)
    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = Role_And_Permission_Serializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response({"Message":"Successfully data deleted"})
class Role_And_Permission_Api_List(generics.ListCreateAPIView):
    search_fields=[]
    filter_backends = (filters.SearchFilter,)
    queryset=Role_And_Permission.objects.all()
    serializer_class=Role_And_Permission_Serializer

class Permission_Show_Search_Api(generics.ListAPIView):
    search_fields=['id','codename','name']
    filter_backends=(filters.SearchFilter,)
    
    queryset=Permission.objects.all()
    serializer_class=Permission_Serializer

class Manufacture_Member_Api(APIView):
    def get(self,request):
        manufacture=Registration_All.objects.filter(role__group__name='Manufacture/Seller')
        serailizer=Registration_All_Show_Serializer(manufacture,many=True)
        
        return Response(serailizer.data)

class Buyer_Member_Api(APIView):
    def get(self,request):
        manufacture=Registration_All.objects.filter(role__group__name='Buyer')
        serailizer=Registration_All_Show_Serializer(manufacture,many=True)
        
        return Response(serailizer.data)

class Both_Member_Api(APIView):
    def get(self,request):
        manufacture=Registration_All.objects.filter(role__group__name='Both')
        serailizer=Registration_All_Show_Serializer(manufacture,many=True)
        
        return Response(serailizer.data)



class Blacklisted_Api_Detail(APIView):
    def get_object(self,pk):
        try:
            return Blacklisted.objects.get(id=pk)
        except Blacklisted.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = Blacklisted_Serializer(snippet)
        return Response(serializer.data)
    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = Blacklisted_Serializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response({"Message":"Successfully data deleted"})
class Blacklisted_Member_Api_List(generics.ListAPIView):
    search_fields=['id','email','try_count','wrong_password','datetime']
    filter_backends=(filters.SearchFilter,)
    queryset=Blacklisted.objects.all()
    serializer_class=Blacklisted_Serializer


class Update_Message_Api_Detail(APIView):
    def get_object(self,pk):
        try:
            return Update_Message.objects.get(id=pk)
        except Update_Message.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = Update_Message_Serializer(snippet)
        return Response(serializer.data)
    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = Update_Message_Serializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response({"Message":"Successfully data deleted"})
class Update_Message_Api_List(generics.ListCreateAPIView):
    search_fields=['id','message','time']
    filter_backends=(filters.SearchFilter,)
    queryset=Update_Message.objects.all()
    serializer_class=Update_Message_Serializer


class Admin_Register_Api(APIView):
    def post(self,request):
        serializer=User_Serializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()

            return Response(serializer.data)
        return Response(serializer.errors)

class Admin_login_Api(APIView):
    #permission_classes=[IsAuthenticated,]
    def post(self,request):
        username=request.data['username']
        password=request.data['password']

        user=User.objects.filter(username=username).first()
        if user == None:
            return Response({"Message":"User Not Found !"})
        if not user.check_password(password):
            return Response({"Message":"Incorrect Password !"})
        
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key}, status=status.HTTP_200_OK)
    
class Logout_Admin_User_Api(APIView):
    def post(request):

        if(request.user.auth_token.delete()):

            return Response({"Message":"You are logged Out"},status=status.HTTP_200_OK)
        return Response({"Message":"Auth has no attribute"})