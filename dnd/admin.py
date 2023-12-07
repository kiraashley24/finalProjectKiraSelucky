from django.contrib import admin
from .models import Race, DndClass

# Register your models here.
class RaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'ability_score', 'lifespan', 'size', 'speed', 'alignment', 'racial_traits')
    search_fields = ['name', 'ability_score', 'lifespan', 'size', 'speed', 'alignment', 'racial_traits']

class DndClassAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'hit_die', 'primary_ability', 'saving_throw_proficiencies', 'armor_proficiencies', 'weapon_proficiencies')
    search_fields = ['name', 'description', 'hit_die', 'primary_ability', 'saving_throw_proficiencies', 'armor_proficiencies', 'weapon_proficiencies']

admin.site.register(Race, RaceAdmin)
admin.site.register(DndClass, DndClassAdmin)