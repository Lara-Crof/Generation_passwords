import http
from django.shortcuts import render
import random

def home(request):
    return render (request, 'generator/home.html')

def auther(request):
    return render(request, 'generator/auther.html')

def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()'))
    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))

    lenght = int(request.GET.get('lenght', 12))
    thepassword = ""
    for x in range(lenght):
        thepassword += random.choice(characters)
    return render (request, 'generator/password.html', {'password':thepassword})

    

# Create your views here.
