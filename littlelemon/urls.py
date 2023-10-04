"""littlelemon URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from rest_framework.authtoken.views import obtain_auth_token
from restaurant.views import MenuViewSet, BookingsViewSet

router = DefaultRouter()
router.register(r'menu', MenuViewSet)
router.register(r'bookings', BookingsViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('restaurant.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    
    # APIs
    # Register for new account:                     # POST--> 'http://localhost:8000/auth/users/' -username -password -email (optional)
    path('api-token-auth/', obtain_auth_token),     # POST -username -password
    path('api/', include(router.urls)),
]
