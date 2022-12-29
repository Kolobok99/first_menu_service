from django.views.generic import ListView, DetailView

from menus.models import Menu


class MenuList(ListView):
    template_name = 'menu-list.html'
    context_object_name = 'menus'

    def get_queryset(self):
        return Menu.objects.filter(parent__isnull=True)


class MenuDetail(DetailView):

    template_name = 'menu-detail.html'
    model = Menu
    context_object_name = 'menu'
    slug_url_kwarg = 'title'
    slug_field = 'title'

# class ItemDetail(DetailView):
#
#     template_name = 'item-detail.html'
#     model = Menu
#     context_object_name = 'item'
#     slug_url_kwarg = 'title'
#
#
#     def get_object(self, queryset=None):
