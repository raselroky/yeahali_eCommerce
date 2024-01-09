from django.urls import path,include
from .import views

urlpatterns = [
    path('addproductapil/',views.Add_Product_Api_List.as_view() ), #create data
    path('addproductshowallapil/',views.Add_Product_Show_All_Api_List.as_view() ), #show all object and search
    path('addproductapid/<int:pk>',views.Add_Product_Api_Detail.as_view() ), #get,put,delete by pk

    path('imageuploadapil/',views.Image_Upload_Api_List.as_view()),
]
