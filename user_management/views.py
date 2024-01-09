from django.shortcuts import render
from rest_framework import generics,status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Registration_All
from .serializers import Registration_All_Serializer
from django.http import Http404
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
from rest_framework import filters


class Registration_All_Api_Detail(APIView):
    def get_object(self,pk):
        try:
            return Registration_All.objects.get(id=pk)
        except Registration_All.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = Registration_All_Serializer(snippet)
        return Response(serializer.data)
    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = Registration_All_Serializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response({"Message":"Successfully data deleted"})

class Registration_All_Api_List(generics.ListCreateAPIView):
    search_fields=['id','first_name','last_name','email','country','address','mobile','gender','marital_status','date_of_joining','role']
    filter_backends = (filters.SearchFilter,)
    queryset=Registration_All.objects.all()
    serializer_class=Registration_All_Serializer


class Login_Api(APIView):
    def post(self,request):
        email=request.data['email']
        password=request.data['password']

        if(Registration_All.objects.filter(email=email).exists()):
            usr=Registration_All.objects.get(email=email)
            if check_password(password, usr.password):
            #print(usr)
                serializer=Registration_All_Serializer(usr)
                if(serializer.data['image']):
                    return Response(serializer.data['image'])
                elif(serializer.data['email']):
                    return Response(serializer.data['email'])
                else:
                    return Response({"Message":"Please fill-up this form"})
                
                    
            else:
                return Response({"Message":"Password Does not Matched"})
            
        return Response({"Message":"Plz register,this username or email does not exist"})
        
    