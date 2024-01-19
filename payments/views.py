from django.shortcuts import render,redirect
from paypal.standard.forms import PayPalPaymentsForm
from django.conf import settings
from django.urls import reverse
from django.contrib import messages

def home(request):

    return render(request,'home.html')
