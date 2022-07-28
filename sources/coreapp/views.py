from django.http import Http404, HttpResponse, HttpResponseNotFound
from django.shortcuts import get_object_or_404, redirect, render
from coreapp.models import Categories, Languages


def page_404(request, exception):
    return HttpResponseNotFound('Страница не найдена!')


def index(request):
    posts = Languages.objects.all()
    context = {
        'posts': posts,
        'cat_selected': 0,
        'title': 'Index Page',
    }
    return render(request, 'coreapp/index.html', context=context)


def show_category(request, cat_id): 
    posts = Languages.objects.filter(cat_id=cat_id)
    
    if len(posts) == 0: 
        raise Http404()
    
    context = {
        'posts': posts,
        'cat_selected': cat_id,
        'title': 'Category Page',
    }
    return render(request, 'coreapp/index.html', context=context)


def show_post(request, post_id): 
    post = get_object_or_404(Languages, pk=post_id)
    context = {
        'post': post,
        'title': post.title,
        'cat_selected': post.cat_id,
    }
    return render(request, 'coreapp/post.html', context=context)


def about(request): return HttpResponse("about page")
def add_page(request): return HttpResponse("add_page page")
def contact(request): return HttpResponse("contact page")
def login(request): return HttpResponse("login page")