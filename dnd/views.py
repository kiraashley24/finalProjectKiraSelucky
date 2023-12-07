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

def class_detail(request, class_name):
    class_name_lower = class_name.lower()
    dnd_class = DndClass.objects.get(name=class_name)
    return render(request, f'class_templates/{class_name_lower}.html', {'class': dnd_class})

def charbuild(request):
    # Add logic for character building, if needed
    return render(request, 'charbuild.html')

def character(request, character_id):
    # Add logic to fetch details of a specific character
    return render(request, 'character.html', {'character_id': character_id})