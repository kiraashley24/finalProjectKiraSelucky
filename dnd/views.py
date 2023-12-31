#INF 601 - Advanced Programming in Python
#Kira Selucky
#Final Project

from django.shortcuts import render, get_object_or_404
from .models import Race, DndClass, BarbarianDetail, BardDetail, ClericDetail, DruidDetail, FighterDetail, MonkDetail, PaladinDetail, RangerDetail, RogueDetail, SorcererDetail, WarlockDetail, WizardDetail
import requests
from .forms import CharacterForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required


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

def character(request, character_id):
    # Add logic to fetch details of a specific character
    return render(request, 'character.html', {'character_id': character_id})

def charbuild(request):
    if request.method == 'POST':
        form = CharacterForm(request.POST)
        submit_action = request.POST.get('submit_action')

        if submit_action == 'Generate Random Name and Age':
            initial_values = generate_random_name_and_age()
            form = CharacterForm(initial=initial_values)
        elif submit_action == 'Create Character' and form.is_valid():
            form.save()
            character_data = {
                'name': form.cleaned_data['name'],
                'age': form.cleaned_data['age'],
                'race': form.cleaned_data['race'],
                'classes': form.cleaned_data['classes'],
                'backstory': form.cleaned_data['backstory'],
            }

            return render(request, 'character.html', {'character_data': character_data})

    else:
        form = CharacterForm()

    return render(request, 'charbuild.html', {'form': form})

def generate_random_name_and_age():
    try:
        url = "https://random-user-data.p.rapidapi.com/getuser"
        headers = {
            "X-RapidAPI-Key": "303803f6d2msh62816098927e1e5p1143a8jsn4e212fe65712",
            "X-RapidAPI-Host": "random-user-data.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers)
        response.raise_for_status()

        data = response.json()
        name = data.get("name")
        age = data.get("age")

        return {'name': name, 'age': age}
    except requests.exceptions.HTTPError as errh:
        # Handle HTTP errors
        print(f"HTTP Error: {response.status_code} - {response.text}")
    except requests.exceptions.RequestException as err:
        # Handle other request errors
        print(f"Request Exception: {err}")

    # Return default values if an error occurs
    return {'name': "John Doe", 'age': "25"}

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful. Welcome!')
            return render(request, 'registration/register.html', {'registration_success': True})
        else:
            for error in form.errors.values():
                messages.error(request, error[0])

    else:
        form = UserCreationForm()

    return render(request, 'registration/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('charbuild')  # or any other success URL
        else:
            messages.add_message(request, messages.ERROR, 'Invalid Credentials. Please check your username and password.')


    else:
        form = AuthenticationForm()

    return render(request, 'registration/login.html', {'form': form})

@login_required
def charbuild(request):
    if request.method == 'POST':
        form = CharacterForm(request.POST)
        submit_action = request.POST.get('submit_action')

        if submit_action == 'Generate Random Name and Age':
            initial_values = generate_random_name_and_age()
            form = CharacterForm(initial=initial_values)
        elif submit_action == 'Create Character' and form.is_valid():
            form.save()
            character_data = {
                'name': form.cleaned_data['name'],
                'age': form.cleaned_data['age'],
                'race': form.cleaned_data['race'],
                'classes': form.cleaned_data['classes'],
                'backstory': form.cleaned_data['backstory'],
            }

            return render(request, 'character.html', {'character_data': character_data})

    else:
        form = CharacterForm()

    return render(request, 'charbuild.html', {'form': form})
