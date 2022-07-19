# from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseNotFound

# Create your views here.
def index(request):
    return HttpResponse('Страница index')

def categories(request, id):
    if request.GET:
        print(request.GET)
    return HttpResponse(f'Страница categories, {id}')

def archive(request, year):
    if int(year) > 2022:
        raise Http404()
    return HttpResponse(f'Страница archive, {year}')

def page_404(request, exception):
    return HttpResponseNotFound('Страница не найдена!')
    