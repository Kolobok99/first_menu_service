from django.contrib import admin
from django.urls import path, include

from menus import urls as menus_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(menus_urls)),

    path(r'_nested_admin/', include('nested_admin.urls')),
    path('__debug__/', include('debug_toolbar.urls')),
]
