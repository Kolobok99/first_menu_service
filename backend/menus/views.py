from django.views.generic import ListView

from menus.models import MenuItem


class MenuList(ListView):
    template_name = 'menu-list.html'
    context_object_name = 'menus'
    slug_url_kwarg = 'title'

    def get_queryset(self):
        return MenuItem.objects.filter(parent__isnull=True)
