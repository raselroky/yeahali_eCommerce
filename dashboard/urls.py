from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,

)
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
 
    #path('api-token/login', TokenObtainPairView.as_view(), name='login-token'), #get token access for login
    #path('loginapi/',obtain_auth_token,name='login'),
    #path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('adminregisterapi/',views.Admin_Register_Api.as_view(),name='register'),
    path('adminloginapi/',views.Admin_login_Api.as_view(),name='login'),
    path('log-out/',views.Logout_Admin_User_Api.as_view(),name='logged-out'),

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