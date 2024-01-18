from django.shortcuts import render
from rest_framework import generics,status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Contact_Us
from .serializers import Contact_Us_Serializer
from django.http import Http404
from rest_framework import filters



class Contact_Us_Api_Detail(APIView):
    def get_object(self,pk):
        try:
            return Contact_Us.objects.get(id=pk)
        except Contact_Us.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = Contact_Us_Serializer(snippet)
        return Response(serializer.data)
    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = Contact_Us_Serializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response({"Message":"Successfully data deleted"})

class Contact_Us_Api_List(generics.ListCreateAPIView):
    search_fields=['name','email','reason','message','dates']
    filter_backends = (filters.SearchFilter,)
    queryset=Contact_Us.objects.all()
    serializer_class=Contact_Us_Serializer