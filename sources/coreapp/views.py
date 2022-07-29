from django.http import Http404, HttpResponse, HttpResponseNotFound
from django.shortcuts import get_object_or_404, redirect, render
from coreapp.models import Categories, Languages
from coreapp.forms import *

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


def show_post(request, post_slug): 
    post = get_object_or_404(Languages, slug=post_slug)
    context = {
        'post': post,
        'title': post.title,
        'cat_selected': post.cat_id,
    }
    return render(request, 'coreapp/post.html', context=context)


def add_page(request): 
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            #print(form.cleaned_data)
            try:
                Languages.objects.create(**form.cleaned_data)
                return redirect('index')
            except:
                form.add_error(None, 'Error: can not insert into database!')

    else:
        form = AddPostForm()
        
    context = {
        'title': 'Add new page',
        'form': form,
    }
    return render(request, 'coreapp/add_page.html', context=context)


def about(request): return HttpResponse("about page")
def contact(request): return HttpResponse("contact page")
def login(request): return HttpResponse("login page")