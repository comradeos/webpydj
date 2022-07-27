from django import template
from coreapp.models import *

register = template.Library()

@register.simple_tag()
def get_categories(filter=None):
    if not filter:
        return Categories.objects.all()
    else:
        return Categories.objects.filter(pk=filter)
    
@register.inclusion_tag('coreapp/list_categories.html')
def show_categories():
    cats = Categories.objects.all()
    return {'cats': cats}