from django.urls import path
from .import views


urlpatterns = [
    path('contactusapil/',views.Contact_Us_Api_List.as_view()),
    path('contactusapid/<int:pk>',views.Contact_Us_Api_Detail.as_view()),
    #path('showapi/',views.Registration_All_Api_Show.as_view()),

    
]