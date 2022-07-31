from django.http import Http404, HttpResponse, HttpResponseNotFound
from django.shortcuts import get_object_or_404, redirect, render
from coreapp.models import Categories, Languages
from coreapp.forms import *
from django.views.generic import ListView, DetailView

def page_404(request, exception):
    return HttpResponseNotFound('Страница не найдена!')

class LanguagesHome(ListView):
    '''Создание представления на основе класса.
    '''
    model = Languages # модель 
    template_name = 'coreapp/index.html' # имя шаблона для использования
    context_object_name = 'posts' # передать данные как коллекцию с именем posts

    def get_context_data(self, **kwargs): 
        '''Передача дополнительных элементов в шаблон
        '''
        context = super().get_context_data(**kwargs)
        context['title'] = 'Index page' # заголовок страницы
        context['cat_selected'] = 0 # выбранная категория
        return context        
    
    def get_queryset(self):
        return Languages.objects.filter(is_published=True)
              
              
# def index(request):
#     posts = Languages.objects.all()
#     context = {
#         'posts': posts,
#         'cat_selected': 0,
#         'title': 'Index Page',
#     }
#     return render(request, 'coreapp/index.html', context=context)


class LanguagesCategory(ListView):
    model = Languages
    template_name = 'coreapp/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        context['title'] = 'Категория - ' + str(context['posts'][0].cat)
        context['cat_selected'] = context['posts'][0].cat_id
        return context        
    
    def get_queryset(self):
        return Languages.objects.filter(cat_id__slug=self.kwargs['cat_slug'], is_published=True)
  
  
    
# def show_category(request, cat_id): 
#     posts = Languages.objects.filter(cat_id=cat_id)
    
#     if len(posts) == 0: 
#         raise Http404()
    
#     context = {
#         'posts': posts,
#         'cat_selected': cat_id,
#         'title': 'Category Page',
#     }
#     return render(request, 'coreapp/index.html', context=context)



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
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
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