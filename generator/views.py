from django.shortcuts import render
import random


# Create your views here.

def home(request):

    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('specialchar'):
        characters.extend(list('!@#$%^&*()'))
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

    length = int(request.GET.get('length',12))

    PasswordGen = ''
    for x in range(length):
        PasswordGen += random.choice(characters)

    return render(request, 'generator/home.html',  {'password':PasswordGen} )