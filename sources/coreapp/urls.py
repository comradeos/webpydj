from django.urls import path, re_path

from coreapp.views import *

urlpatterns = [
    path('', index),
    path('categories/<str:id>/', categories), # <str: int: slug: uuid: path:>
    re_path(r'^archive/(?P<year>[0-9]{4})/', archive),
]
