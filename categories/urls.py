from django.urls import path,include
from .import views

urlpatterns = [
    path('brandapil/',views.Brand_Api_List.as_view()), #search and create and show all object
    path('brandapid/<int:pk>',views.Brand_Api_Detail.as_view()), #get,put,delete by pk

    path('categoryapil/',views.Category_Api_List.as_view()), #create data
    path('categoryshowallapi/',views.Category_Show_All_Api_List.as_view()), #search and show all object in display
    path('categoryapid/<int:pk>',views.Category_Api_Detail.as_view()), #get,put,delete by pk

    path('subcategoryapil/',views.SubCategory_Api_List.as_view()), #create data
    path('subcategoryshowallapi/',views.SubCategory_Show_All_Api_List.as_view()), #search and show all object in display
    path('subcategoryapid/<int:pk>',views.SubCategory_Api_Detail.as_view()), #get,put,delete by pk
    
]