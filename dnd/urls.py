from django.urls import path
from .views import index, races, classes, charbuild, character

urlpatterns = [
    path('', index, name='index'),
    path('races/', races, name='races'),
    path('classes/', classes, name='classes'),
    path('charbuild/', charbuild, name='charbuild'),
    path('character/<int:character_id>/', character, name='character'),
]