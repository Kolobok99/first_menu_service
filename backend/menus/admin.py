import nested_admin

from django.contrib import admin

from .models import Menu


class MenuItemInline(nested_admin.NestedStackedInline):
    model = Menu
    extra = 3


class MenuItemAdmin(nested_admin.NestedModelAdmin):
    inlines = [MenuItemInline]


admin.site.register(Menu, MenuItemAdmin)
