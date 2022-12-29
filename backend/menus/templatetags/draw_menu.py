from django import template

from menus.models import Menu

register = template.Library()

@register.inclusion_tag('tags/draw_menu.html')
def draw_menu(*args):

    title = args[0]

    menu = Menu.objects.get(title=title)
    children = menu.get_descendants(include_self=True)

    return {'menus': children}

