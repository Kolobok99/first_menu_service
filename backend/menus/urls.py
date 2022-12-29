from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.MenuList.as_view(), name='menu-list'),
    path('menu/<str:title>/', views.MenuDetail.as_view(), name='menu-detail'),
]
