from django.urls import path
from . import views


urlpatterns = [

    path('adminloginapi/',views.Admin_Login_Api.as_view()),

    path('rolesapil/',views.Role_And_Permission_Api_List.as_view()),
    path('rolesapid/<int:pk>',views.Role_And_Permission_Api_Detail.as_view()),
    path('permissionallshowapil/',views.Permission_Show_Search_Api.as_view()),

    path('manufacturememberapil/',views.Manufacture_Member_Api.as_view()),
    path('buyermemberapil/',views.Buyer_Member_Api.as_view()),
    path('bothmemberapil/',views.Both_Member_Api.as_view()),

    path('blacklistapil/',views.Blacklisted_Member_Api_List.as_view()),
    path('blacklistapid/<int:pk>',views.Blacklisted_Api_Detail.as_view()),

    path('updatemessageapil/',views.Update_Message_Api_List.as_view()),
    path('updatemessageapid/<int:pk>',views.Update_Message_Api_Detail.as_view()),

    
]