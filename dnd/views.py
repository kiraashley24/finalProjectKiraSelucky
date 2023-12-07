from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Race, DndClass, BarbarianDetail, BardDetail, ClericDetail, DruidDetail, FighterDetail, MonkDetail, PaladinDetail, RangerDetail, RogueDetail, SorcererDetail, WarlockDetail, WizardDetail

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
    dnd_class = get_object_or_404(DndClass, name=class_name)

    # Query details based on the class name
    class_details = None
    if class_name_lower == 'barbarian':
        class_details = BarbarianDetail.objects.all()
    elif class_name_lower == 'bard':
        class_details = BardDetail.objects.all()
    elif class_name_lower == 'cleric':
        class_details = ClericDetail.objects.all()
    elif class_name_lower == 'druid':
        class_details = DruidDetail.objects.all()
    elif class_name_lower == 'fighter':
        class_details = FighterDetail.objects.all()
    elif class_name_lower == 'monk':
        class_details = MonkDetail.objects.all()
    elif class_name_lower == 'paladin':
        class_details = PaladinDetail.objects.all()
    elif class_name_lower == 'ranger':
        class_details = RangerDetail.objects.all()
    elif class_name_lower == 'rogue':
        class_details = RogueDetail.objects.all()
    elif class_name_lower == 'sorcerer':
        class_details = SorcererDetail.objects.all()
    elif class_name_lower == 'warlock':
        class_details = WarlockDetail.objects.all()
    elif class_name_lower == 'wizard':
        class_details = WizardDetail.objects.all()

    return render(request, f'class_templates/{class_name_lower}.html',
                  {'class': dnd_class, 'class_details': class_details})

def charbuild(request):
    # Add logic for character building, if needed
    return render(request, 'charbuild.html')

def character(request, character_id):
    # Add logic to fetch details of a specific character
    return render(request, 'character.html', {'character_id': character_id})