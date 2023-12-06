from django.db import models

# Create your models here.
class Race(models.Model):
    name = models.CharField(max_length=50)
    # Add other fields as needed
    def __str__(self):
        return self.name

class DndClass(models.Model):
    name = models.CharField(max_length=50)
    # Add other fields as needed
    def __str__(self):
        return self.name