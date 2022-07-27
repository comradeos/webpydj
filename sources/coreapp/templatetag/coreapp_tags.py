from django import template
from coreapp.models import *

register = template.Library()

def get_categories():
    return Categories.objects.all()