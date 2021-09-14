"""Hireme URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path,include
from rest_framework import routers
from api.views import (
HeroListApi,
HeroGetApi,
JobsListApi,
ClientGetApi,
AcceptedListApi,
HiringListApi,
)

# router = routers.DefaultRouter()
# router.register(r'heros',HeroListApi,basename='heros')
# router.register(r'hero/<int:pk>',HeroGetApi,basename='hero')
# router.register(r'user/<int:pk>',ClientGetApi,basename='client')
# router.register(r'jobs',JobsListApi,basename='jobs')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('heros/',HeroListApi.as_view()),
    path('hero/<int:pk>/',HeroGetApi.as_view()),
    path('user/<int:pk>/',ClientGetApi.as_view()),
    path('jobs/',JobsListApi.as_view()),
    path('hirings/',HiringListApi.as_view()),
    path('acceptance/',AcceptedListApi.as_view()),

]
