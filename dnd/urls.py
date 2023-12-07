from django.urls import path
from .views import index, races, classes, class_detail, charbuild, character

app_name = 'dnd'

urlpatterns = [
    path('', index, name='index'),
    path('races/', races, name='races'),
    path('classes/', classes, name='classes'),
    path('class/<str:class_name>/', class_detail, name='class_detail'),
    path('charbuild/', charbuild, name='charbuild'),
    path('character/<int:character_id>/', character, name='character'),
]