from django.urls import path

from coreapp.views import *

urlpatterns = [
    path('', index),
    path('categories/', categories),
]
