from django.shortcuts import render
from rest_framework import generics,status
from rest_framework.views import APIView,Response
from django.http import Http404
from rest_framework import filters
from .serializers import Brand_Serializer,Category_Serializer,SubCategory_Serializer,Category_Show_All_Serializer,SubCategory_Show_All_Serializer
from .models import Brand,Category,SubCategory


class Brand_Api_Detail(APIView):
    def get_object(self,pk):
        try:
            return Brand.objects.get(id=pk)
        except Brand.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = Brand_Serializer(snippet)
        return Response(serializer.data)
    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = Brand_Serializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response({"Message":"Successfully data deleted"})

class Brand_Api_List(generics.ListCreateAPIView):
    search_fields=['id','brand_name','short_description']
    filter_backends=(filters.SearchFilter,)
    queryset=Brand.objects.all()
    serializer_class=Brand_Serializer



class Category_Api_Detail(APIView):
    def get_object(self,pk):
        try:
            return Category.objects.get(id=pk)
        except Category.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = Category_Serializer(snippet)
        return Response(serializer.data)
    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = Category_Serializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response({"Message":"Successfully data deleted"})

class Category_Api_List(generics.ListCreateAPIView):
    #search_fields=['id','category_name','description','brand__brand_name','brand__short_description']
    #filter_backends=(filters.SearchFilter,)
    queryset=Category.objects.all()
    serializer_class=Category_Serializer
class Category_Show_All_Api_List(generics.ListAPIView):
    search_fields=['id','category_name','description','brand__brand_name','brand__short_description']
    filter_backends=(filters.SearchFilter,)
    queryset=Category.objects.all()
    serializer_class=Category_Show_All_Serializer




class SubCategory_Api_Detail(APIView):
    def get_object(self,pk):
        try:
            return SubCategory.objects.get(id=pk)
        except SubCategory.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = SubCategory_Serializer(snippet)
        return Response(serializer.data)
    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = SubCategory_Serializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response({"Message":"Successfully data deleted"})

class SubCategory_Api_List(generics.ListCreateAPIView):
    #search_fields=['id','subcategory_name','category__category_name','category__description']
    #filter_backends=(filters.SearchFilter,)
    queryset=SubCategory.objects.all()
    serializer_class=SubCategory_Serializer
class SubCategory_Show_All_Api_List(generics.ListAPIView):
    search_fields=['id','subcategory_name','category__category_name','category__description']
    filter_backends=(filters.SearchFilter,)
    queryset=SubCategory.objects.all()
    serializer_class=SubCategory_Show_All_Serializer