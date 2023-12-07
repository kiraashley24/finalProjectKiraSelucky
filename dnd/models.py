from django.db import models

# Create your models here.
class Race(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    ability_score = models.CharField(max_length=50, null=True, blank=True)
    lifespan = models.CharField(max_length=50, null=True, blank=True)
    size = models.CharField(max_length=50, null=True, blank=True)
    speed = models.CharField(max_length=50, null=True, blank=True)
    alignment = models.CharField(max_length=500, null=True, blank=True)
    racial_traits = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class DndClass(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    hit_die = models.CharField(max_length=50, null=True, blank=True)
    primary_ability = models.CharField(max_length=50, null=True, blank=True)
    saving_throw_proficiencies = models.CharField(max_length=255, null=True, blank=True)
    armor_proficiencies = models.CharField(max_length=255, null=True, blank=True)
    weapon_proficiencies = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name