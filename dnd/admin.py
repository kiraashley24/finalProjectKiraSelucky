from django.contrib import admin
from .models import Race, Charbuild, DndClass, BarbarianDetail, BardDetail, ClericDetail, DruidDetail, FighterDetail, MonkDetail, PaladinDetail, RangerDetail, RogueDetail, SorcererDetail, WarlockDetail, WizardDetail

# Register your models here.
class RaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'ability_score', 'lifespan', 'size', 'speed', 'alignment', 'racial_traits')
    search_fields = ['name', 'ability_score', 'lifespan', 'size', 'speed', 'alignment', 'racial_traits']

class DndClassAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'hit_die', 'primary_ability', 'saving_throw_proficiencies', 'armor_proficiencies', 'weapon_proficiencies')
    search_fields = ['name', 'description', 'hit_die', 'primary_ability', 'saving_throw_proficiencies', 'armor_proficiencies', 'weapon_proficiencies']

class BarbarianDetailAdmin(admin.ModelAdmin):
    list_display = ('level', 'proficiency_bonus', 'features', 'rages', 'rage_damage')

class CharbuildAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'race', 'classes', 'backstory')



admin.site.register(Race, RaceAdmin)
admin.site.register(DndClass, DndClassAdmin)
admin.site.register(Charbuild, CharbuildAdmin)
admin.site.register(BarbarianDetail)
admin.site.register(BardDetail)
admin.site.register(ClericDetail)
admin.site.register(DruidDetail)
admin.site.register(FighterDetail)
admin.site.register(MonkDetail)
admin.site.register(PaladinDetail)
admin.site.register(RangerDetail)
admin.site.register(RogueDetail)
admin.site.register(SorcererDetail)
admin.site.register(WarlockDetail)
admin.site.register(WizardDetail)