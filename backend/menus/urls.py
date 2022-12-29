from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('menus', views.MenuList.as_view(), name='menu-list'),
    path('menus/<str:title>/', views.MenuDetail.as_view(), name='menu-detail'),
]
