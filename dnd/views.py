from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Race, DndClass, BarbarianDetail, BardDetail, ClericDetail, DruidDetail, FighterDetail, MonkDetail, PaladinDetail, RangerDetail, RogueDetail, SorcererDetail, WarlockDetail, WizardDetail
import requests
from .forms import CharacterForm
from django.shortcuts import render, redirect
from requests.exceptions import HTTPError, RequestException, JSONDecodeError


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


def charbuild_random(request):
    try:
        url = "https://random-user-data.p.rapidapi.com/getuser"
        headers = {
            "X-RapidAPI-Key": "303803f6d2msh62816098927e1e5p1143a8jsn4e212fe65712",
            "X-RapidAPI-Host": "random-user-data.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers)
        response.raise_for_status()

        data = response.json()
        user_data = {
            "name": data.get("name"),
            "age": data.get("age"),
            # Include other fields as needed
        }

        return render(request, "charbuild.html", {"user_data": user_data})
    except requests.exceptions.HTTPError as errh:
        return render(request, "charbuild.html", {"error_message": f"HTTP Error: {response.status_code} - {response.text}"})
    except requests.exceptions.RequestException as err:
        return render(request, "charbuild.html", {"error_message": f"Request Exception: {err}"})


def character(request, character_id):
    # Add logic to fetch details of a specific character
    return render(request, 'character.html', {'character_id': character_id})


def charbuild(request):
    if request.method == 'POST':
        form = CharacterForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return redirect('index')  # Redirect to the desired page after form submission
    else:
        form = CharacterForm()

    return render(request, 'charbuild.html', {'form': form})
