from django.http import Http404, HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect, render
from coreapp.models import Languages


menu = [
    {'title': 'About', 'url_name': 'about', },
    {'title': 'Add Page', 'url_name': 'add_page', },
    {'title': 'Contact', 'url_name': 'contact', },
    {'title': 'Login', 'url_name': 'login', },
]


def index(request):
    posts = Languages.objects.all()
    return render(request, 'coreapp/index.html',
                  context={
                      'menu': menu,
                      'posts': posts,
                      'title': 'Index Page',
                  })


def about(request):
    return render(request, 'coreapp/about.html', {'menu': menu, 'title': 'About Page', })


def categories(request, id):
    if request.GET:
        print(request.GET)
    return HttpResponse(f'Страница categories, {id}')


def archive(request, year):
    if int(year) > 2022:
        return redirect('home', permanent=True)  # 301 == permanent=True
        # raise Http404()
    return HttpResponse(f'Страница archive, {year}')


def page_404(request, exception):
    return HttpResponseNotFound('Страница не найдена!')
