# from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def coreapp(request):
    return HttpResponse('Страница coreapp')

def categories(request):
    return HttpResponse('Страница categories')