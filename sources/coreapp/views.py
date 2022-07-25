from django.http import Http404, HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect, render
from coreapp.models import Categories, Languages


menu = [
    {'title': 'About', 'url_name': 'about', },
    {'title': 'Add Page', 'url_name': 'add_page', },
    {'title': 'Contact', 'url_name': 'contact', },
    {'title': 'Login', 'url_name': 'login', },
]


def page_404(request, exception):
    return HttpResponseNotFound('Страница не найдена!')


def index(request):
    posts = Languages.objects.all()
    cats = Categories.objects.all()
    context = {
        'menu': menu,
        'posts': posts,
        'cats': cats,
        'cat_selected': 0,
        'title': 'Index Page',
    }
    return render(request, 'coreapp/index.html', context=context)


def about(request): return HttpResponse("about page")
def add_page(request): return HttpResponse("add_page page")
def contact(request): return HttpResponse("contact page")
def login(request): return HttpResponse("login page")
def show_post(request, post_id): return HttpResponse(f"show_post id {post_id}")

def show_category(request, cat_id): 
    posts = Languages.objects.filter(cat_id=cat_id)
    cats = Categories.objects.all()
    
    if len(posts) == 0: 
        raise Http404()
    
    context = {
        'menu': menu,
        'posts': posts,
        'cats': cats,
        'cat_selected': cat_id,
        'title': 'Category Page',
    }
    return render(request, 'coreapp/index.html', context=context)
