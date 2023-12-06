from django.http import HttpResponse
from django.shortcuts import render
from .models import Race, DndClass

def index(request):
    return render(request, 'index.html')

def races(request):
    races = Race.objects.all()
    return render(request, 'races.html', {'races': races})

def classes(request):
    classes = DndClass.objects.all()
    return render(request, 'classes.html', {'classes': classes})

def charbuild(request):
    # Add logic for character building, if needed
    return render(request, 'charbuild.html')

def character(request, character_id):
    # Add logic to fetch details of a specific character
    return render(request, 'character.html', {'character_id': character_id})