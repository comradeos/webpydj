from django.http import Http404, HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect, render


menu = [
    'About',
    'New Article',
    'Contact',
    'Login',
]



def index(request):
    return render(request, 'coreapp/index.html', {'menu': menu, 'title': 'Index Page',})

def about(request):
    return render(request, 'coreapp/about.html', {'menu': menu, 'title': 'About Page',})


def categories(request, id):
    if request.GET:
        print(request.GET)
    return HttpResponse(f'Страница categories, {id}')

def archive(request, year):
    if int(year) > 2022:
        return redirect('home', permanent=True) # 301 == permanent=True
        # raise Http404()
    return HttpResponse(f'Страница archive, {year}')

def page_404(request, exception):
    return HttpResponseNotFound('Страница не найдена!')