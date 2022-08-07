from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse_lazy
from coreapp.models import Categories, Languages
from coreapp.forms import *
from django.views.generic import ListView, DetailView, CreateView
from coreapp.utils import DataMixin

from django.contrib.auth.mixins import LoginRequiredMixin

def page_404(request, exception):
    return HttpResponseNotFound('Страница не найдена!')


class LanguagesHome(DataMixin, ListView):
    '''Создание представления на основе класса.
    '''
    model = Languages # модель 
    template_name = 'coreapp/index.html' # имя шаблона для использования
    context_object_name = 'posts' # передать данные как коллекцию с именем posts
    paginate_by = 4

    def get_context_data(self, **kwargs): 
        '''Передача дополнительных элементов в шаблон
        '''
        context = super().get_context_data(**kwargs)
        mix_context = self.get_user_context(title='Index page')
        return dict(list(context.items()) + list(mix_context.items()))
    
    def get_queryset(self):
        return Languages.objects.filter(is_published=True)


class AddPage(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'coreapp/add_page.html'
    success_url = reverse_lazy('index')
    login_url = reverse_lazy('index')
    raise_exception = True # 403
    
    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        mix_context = self.get_user_context(title='Add Page')
        return dict(list(context.items()) + list(mix_context.items()))


class LanguagesCategory(ListView):
    model = Languages
    template_name = 'coreapp/index.html'
    context_object_name = 'posts'
    allow_empty = False
    paginate_by = 4

    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        context['title'] = 'Категория - ' + str(context['posts'][0].cat)
        context['cat_selected'] = context['posts'][0].cat_id
        return context        
    
    def get_queryset(self):
        return Languages.objects.filter(cat_id__slug=self.kwargs['cat_slug'], is_published=True)


class ShowPost(DetailView):
    model = Languages
    template_name = 'coreapp/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        context['title'] = context['post']
        return context        

def about(request): return HttpResponse("about page")
def contact(request): return HttpResponse("contact page")
def login(request): return HttpResponse("login page")
def register(request): return HttpResponse("register page")