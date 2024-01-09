from django.shortcuts import render
from rest_framework import generics,status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from rest_framework import filters
from .models import Add_Product,Image_Upload
from .serializers import Add_Product_Serializer,Image_Upload_Serializer,Add_Product_Show_All_Serializer
from rest_framework.parsers import MultiPartParser, FormParser



class Add_Product_Api_Detail(APIView):
    def get_object(self,pk):
        try:
            return Add_Product.objects.get(id=pk)
        except Add_Product.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = Add_Product_Serializer(snippet)
        return Response(serializer.data)
    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = Add_Product_Serializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response({"Message":"Successfully data deleted"})

class Add_Product_Api_List(generics.ListCreateAPIView):
    #search_fields=['id','product_name','product_description','product_brand__brand_name','product_brand__short_description','product_category__category_name','product_category__description','product_subcategory__subcategory_name','upload_time']
    #filter_backends = (filters.SearchFilter,)
    #permission_classes=[MultiPartParser,FormParser]
    queryset=Add_Product.objects.all()
    serializer_class=Add_Product_Serializer
class Add_Product_Show_All_Api_List(generics.ListAPIView):
    search_fields=['id','product_name','product_description','product_brand__brand_name','product_brand__short_description','product_category__category_name','product_category__description','product_subcategory__subcategory_name','upload_time']
    filter_backends = (filters.SearchFilter,)
    queryset=Add_Product.objects.all()
    serializer_class=Add_Product_Show_All_Serializer


class Image_Upload_Api_List(generics.ListCreateAPIView):
    search_fields=['id','images']
    filter_backends = (filters.SearchFilter,)
    queryset=Image_Upload.objects.all()
    serializer_class=Image_Upload_Serializer