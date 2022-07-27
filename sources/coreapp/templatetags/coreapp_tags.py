from django import template
from coreapp.models import *

register = template.Library()


@register.simple_tag(name='getcats')
def get_categories(filter=None):
    if not filter:
        return Categories.objects.all()
    else:
        return Categories.objects.filter(pk=filter)


@register.inclusion_tag('coreapp/list_categories.html')
def show_categories(sort=None, cat_selected=0):
    if not sort:
        cats = Categories.objects.all()
    else:
        cats = Categories.objects.order_by(sort)
    return {
        'cats': cats,
        'cat_selected': cat_selected,
    }


@register.inclusion_tag('coreapp/menu.html') # в какой файл вернуть значение
def show_menu():
    menu = [
        {'title': 'About', 'url_name': 'about', },
        {'title': 'Add Page', 'url_name': 'add_page', },
        {'title': 'Contact', 'url_name': 'contact', },
        {'title': 'Login', 'url_name': 'login', },
    ]
    return { 'menu': menu, }
