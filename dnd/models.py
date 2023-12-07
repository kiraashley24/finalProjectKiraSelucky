from django.db import models

# Create your models here.
class Race(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    ability_score = models.CharField(max_length=50, null=True, blank=True)
    age = models.CharField(max_length=50, null=True, blank=True)
    size = models.CharField(max_length=50, null=True, blank=True)
    speed = models.CharField(max_length=50, null=True, blank=True)
    alignment = models.CharField(max_length=50, null=True, blank=True)
    racial_traits = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class DndClass(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name