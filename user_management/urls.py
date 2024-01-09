from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
    path('registerapil/',views.Registration_All_Api_List.as_view()),
    path('registerapid/<int:pk>',views.Registration_All_Api_Detail.as_view()),
    #path('showapi/',views.Registration_All_Api_Show.as_view()),

    path('loginapi/',views.Login_Api.as_view()),
]