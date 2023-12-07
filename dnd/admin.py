from django.contrib import admin
from .models import Race, DndClass

# Register your models here.
class RaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'ability_score', 'age', 'size', 'speed', 'alignment', 'racial_traits')
    search_fields = ['name', 'ability_score', 'age', 'size', 'speed', 'alignment', 'racial_traits']

admin.site.register(Race, RaceAdmin)
admin.site.register(DndClass)