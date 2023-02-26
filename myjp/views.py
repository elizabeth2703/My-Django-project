from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    name = 'Elizaveta'

    return render(request, 'homce.html', {'name': name})