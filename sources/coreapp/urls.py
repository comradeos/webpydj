from django.urls import path, re_path

from coreapp.views import *

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('add-page/', add_page, name='add_page'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('post/<int:post_id>/', show_post, name='post'),
    path('category/<int:category_id>/', show_category, name='category'),
]

