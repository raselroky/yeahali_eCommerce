from django.shortcuts import render
from rest_framework import generics,status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Registration_All,Blacklisted
from .serializers import Registration_All_Serializer,Registration_All_Show_Serializer,Blacklisted_Serializer
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
    #search_fields=['id','first_name','last_name','email','country','address','mobile','gender','marital_status','date_of_joining','role']
    #filter_backends = (filters.SearchFilter,)
    queryset=Registration_All.objects.all()
    serializer_class=Registration_All_Serializer

class Registration_All_Show_Api_List(generics.ListAPIView):
    search_fields=['id','first_name','last_name','email','country','address','mobile','gender','marital_status','date_of_joining']
    filter_backends = (filters.SearchFilter,)
    queryset=Registration_All.objects.all()
    serializer_class=Registration_All_Show_Serializer


class Login_Api(APIView):
    
    def post(self,request):
        email=request.data.get('email')
        password=request.data.get('password')

        rg=Registration_All.objects.filter(email=email).exists()
        #print(rg,Registration_All.objects.filter(email=email))
        if(rg==True):
            #active=False
            blacklist=Blacklisted.objects.filter(email=email).exists()
            if(blacklist):
                blacklist1=Blacklisted.objects.get(email=email)
                active=bool(blacklist1.is_active)
            usr=Registration_All.objects.get(email=email)
            ck=check_password(password, usr.password)
            #print(ck)
            if(ck==True and active==True):
                #print(usr)
                serializer=Registration_All_Serializer(usr)
                #print(serializer.data)
                return Response(serializer.data)
            elif(ck==True and active==False):
                return Response({"Your account blocked":"Contact with authority "})
            else:
                blk1=Blacklisted()
                blk=Blacklisted.objects.filter(email=email).exists()
                if(blk==False):
                    blk1.email=email
                    blk1.save()
                blk2=Blacklisted.objects.get(email=email)
                
                count=int(blk2.try_count)
                blk2.try_count=count+1
                ps=str(blk2.wrong_password)
                blk2.wrong_password=ps+' [ '+str(password)+' ], '

                blk2.save()
                if(blk2.try_count>=3):
                    blk2.is_active=False
                    blk2.save()
                    return Response({"Your account blocked":"Contact with authority "})
                return Response({"Message":"Password Does not Matched"})

        else:
            return Response({"Message":"Plz register,this username or email does not exist"})
