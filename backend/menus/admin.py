import nested_admin

from django.contrib import admin

from .models import MenuItem


class MenuItemInline(nested_admin.NestedStackedInline):
    model = MenuItem
    extra = 3


class MenuItemAdmin(nested_admin.NestedModelAdmin):
    inlines = [MenuItemInline]


admin.site.register(MenuItem, MenuItemAdmin)


admin.site.register(MenuItem, MenuItemAdmin)