from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users-api/',include('user_management.urls')),
    path('categories-api/',include('categories.urls')),
    path('products-api/',include('products.urls')),
    path('contact_us-api/',include('contact_us.urls')),
    path('dashboard-api/',include('dashboard.urls')),

    #path('api-token-auth/',views.obtain_auth_token,name='api-token-auth')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)