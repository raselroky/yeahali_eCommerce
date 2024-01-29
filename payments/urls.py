from django.urls import path,include
from .import views

urlpatterns = [

    path('paypal/',views.paypal,name='paypal'),
    path('stripe/',views.stripe,name='stripe'),
    
]
