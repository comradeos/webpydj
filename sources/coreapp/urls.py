from django.urls import path, re_path

from coreapp.views import *

urlpatterns = [
    # path('', index, name='index'),
    path('', LanguagesHome.as_view(), name='index'),
    path('about/', about, name='about'),
    
    # path('add-page/', add_page, name='add_page'),
    path('add-page/', AddPage.as_view(), name='add_page'),
    
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    
    # path('post/<slug:post_slug>/', show_post, name='post'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    
    # path('category/<int:cat_id>/', show_category, name='category'),
    path('category/<slug:cat_slug>/', LanguagesCategory.as_view(), name='category'),
]

