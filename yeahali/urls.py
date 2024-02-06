from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users-api/',include('user_management.urls')),
    path('categories-api/',include('categories.urls')),
    path('products-api/',include('products.urls')),
    path('contact_us-api/',include('contact_us.urls')),
    path('dashboard-api/',include('dashboard.urls')),
    
    path('payments-api/',include('payments.urls')),
    
    #path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    #path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)