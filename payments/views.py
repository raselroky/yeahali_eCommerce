from django.shortcuts import render,redirect
from paypal.standard.forms import PayPalPaymentsForm
from django.conf import settings
from django.urls import reverse
from django.contrib import messages

def paypal(request):
    return render(request,'paypal.html')

def stripe(request):
    return render(request,'stripe.html')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["key"] = settings.STRIPE_PUBLISHABLE_KEY
        return context
    