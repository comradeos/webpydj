# from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Страница index')

def categories(request, id):
    return HttpResponse(f'Страница categories, {id}')

def archive(request, year):
    return HttpResponse(f'Страница archive, {year}')