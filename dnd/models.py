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

class BarbarianDetail(models.Model):
    level = models.IntegerField()
    proficiency_bonus = models.CharField(max_length=10)
    features = models.TextField()
    rages = models.IntegerField()
    rage_damage = models.CharField(max_length=10)

    # Add any other fields needed for Barbarian details

    def __str__(self):
        return f"Barbarian Detail - Level {self.level}"

class BardDetail(models.Model):
    level = models.IntegerField()
    proficiency_bonus = models.CharField(max_length=10)
    features = models.TextField()
    cantrips_known = models.IntegerField()
    spells_known = models.IntegerField()
    spell_1st = models.IntegerField(null=True, blank=True)
    spell_2nd = models.IntegerField(null=True, blank=True)
    spell_3rd = models.IntegerField(null=True, blank=True)
    spell_4th = models.IntegerField(null=True, blank=True)
    spell_5th = models.IntegerField(null=True, blank=True)
    spell_6th = models.IntegerField(null=True, blank=True)
    spell_7th = models.IntegerField(null=True, blank=True)
    spell_8th = models.IntegerField(null=True, blank=True)
    spell_9th = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"Bard Details - Level {self.level}"

class ClericDetail(models.Model):
    level = models.IntegerField()
    proficiency_bonus = models.CharField(max_length=10)
    features = models.TextField()
    cantrips_known = models.IntegerField()
    spell_1st = models.IntegerField(null=True, blank=True)
    spell_2nd = models.IntegerField(null=True, blank=True)
    spell_3rd = models.IntegerField(null=True, blank=True)
    spell_4th = models.IntegerField(null=True, blank=True)
    spell_5th = models.IntegerField(null=True, blank=True)
    spell_6th = models.IntegerField(null=True, blank=True)
    spell_7th = models.IntegerField(null=True, blank=True)
    spell_8th = models.IntegerField(null=True, blank=True)
    spell_9th = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"Cleric Details - Level {self.level}"

class DruidDetail(models.Model):
    level = models.IntegerField()
    proficiency_bonus = models.CharField(max_length=10)
    features = models.TextField()
    cantrips_known = models.IntegerField()
    spells_known = models.IntegerField()
    spell_1st = models.IntegerField(null=True, blank=True)
    spell_2nd = models.IntegerField(null=True, blank=True)
    spell_3rd = models.IntegerField(null=True, blank=True)
    spell_4th = models.IntegerField(null=True, blank=True)
    spell_5th = models.IntegerField(null=True, blank=True)
    spell_6th = models.IntegerField(null=True, blank=True)
    spell_7th = models.IntegerField(null=True, blank=True)
    spell_8th = models.IntegerField(null=True, blank=True)
    spell_9th = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"Druid Details - Level {self.level}"

class FighterDetail(models.Model):
    level = models.IntegerField()
    proficiency_bonus = models.CharField(max_length=10)
    features = models.TextField()

    def __str__(self):
        return f"Fighter Details - Level {self.level}"

class MonkDetail(models.Model):
    level = models.IntegerField()
    proficiency_bonus = models.CharField(max_length=10)
    martial_arts = models.TextField()
    ki_points = models.IntegerField(null=True, blank=True)
    unarmored_movement = models.TextField(null=True, blank=True)
    features = models.TextField()

    def __str__(self):
        return f"Monk Details - Level {self.level}"

class PaladinDetail(models.Model):
    level = models.IntegerField()
    proficiency_bonus = models.CharField(max_length=10)
    features = models.TextField()
    spells_known = models.IntegerField()
    spell_1st = models.IntegerField(null=True, blank=True)
    spell_2nd = models.IntegerField(null=True, blank=True)
    spell_3rd = models.IntegerField(null=True, blank=True)
    spell_4th = models.IntegerField(null=True, blank=True)
    spell_5th = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"Paladin Details - Level {self.level}"

class RangerDetail(models.Model):
    level = models.IntegerField()
    proficiency_bonus = models.CharField(max_length=10)
    features = models.TextField()
    spells_known = models.IntegerField()
    spell_1st = models.IntegerField(null=True, blank=True)
    spell_2nd = models.IntegerField(null=True, blank=True)
    spell_3rd = models.IntegerField(null=True, blank=True)
    spell_4th = models.IntegerField(null=True, blank=True)
    spell_5th = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"Ranger Details - Level {self.level}"

class RogueDetail(models.Model):
    level = models.IntegerField()
    proficiency_bonus = models.CharField(max_length=10)
    sneak_attack = models.CharField(max_length=10)
    features = models.TextField()

    def __str__(self):
        return f"Rogue Details - Level {self.level}"

class SorcererDetail(models.Model):
    level = models.IntegerField()
    proficiency_bonus = models.CharField(max_length=10)
    sorcery_points = models.IntegerField(null=True, blank=True)
    features = models.TextField()
    cantrips_known = models.IntegerField()
    spells_known = models.IntegerField()
    spell_1st = models.IntegerField(null=True, blank=True)
    spell_2nd = models.IntegerField(null=True, blank=True)
    spell_3rd = models.IntegerField(null=True, blank=True)
    spell_4th = models.IntegerField(null=True, blank=True)
    spell_5th = models.IntegerField(null=True, blank=True)
    spell_6th = models.IntegerField(null=True, blank=True)
    spell_7th = models.IntegerField(null=True, blank=True)
    spell_8th = models.IntegerField(null=True, blank=True)
    spell_9th = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"Sorcerer Details - Level {self.level}"

class WarlockDetail(models.Model):
    level = models.IntegerField()
    proficiency_bonus = models.CharField(max_length=10)
    features = models.TextField()
    cantrips_known = models.IntegerField()
    spells_known = models.IntegerField()
    spell_slots = models.IntegerField()
    slot_level = models.CharField(max_length=10)
    invocations_known = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"Warlock Details - Level {self.level}"

class WizardDetail(models.Model):
    level = models.IntegerField()
    proficiency_bonus = models.CharField(max_length=10)
    features = models.TextField()
    cantrips_known = models.IntegerField()
    spell_1st = models.IntegerField(null=True, blank=True)
    spell_2nd = models.IntegerField(null=True, blank=True)
    spell_3rd = models.IntegerField(null=True, blank=True)
    spell_4th = models.IntegerField(null=True, blank=True)
    spell_5th = models.IntegerField(null=True, blank=True)
    spell_6th = models.IntegerField(null=True, blank=True)
    spell_7th = models.IntegerField(null=True, blank=True)
    spell_8th = models.IntegerField(null=True, blank=True)
    spell_9th = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"Wizard Details - Level {self.level}"