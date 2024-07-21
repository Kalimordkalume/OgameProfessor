from django.contrib.auth.models import User
from django.db import models

ACCOUNT_CLASS_CHOICES = {
    "G": "General",
    "D": "Discoverer",
    "M": "Merchant",
}


PLANET_LIFE_FORM_CHOICES = {
    "H": "Human",
    "K": "Kaelesh",
    "M": "Mecha",
    "R": "Rock_Tal",
}

TECHNOLOGIES_CHOICES = {
    "1": "Armor Technology",
    "2": "Intergalactic Technology",
    "3": "Plasma Technology",
}


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(
        max_length=50,
        unique=True,
    )
    account_class = models.CharField(
        max_length=1,
        choices=ACCOUNT_CLASS_CHOICES,
    )
    universe_speed = models.SmallIntegerField(default=1)


class Planet(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    temperature = models.SmallIntegerField(default=0)
    life_form_type = models.CharField(max_length=1, choices=PLANET_LIFE_FORM_CHOICES)


class Technology(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    name = models.CharField(choices=TECHNOLOGIES_CHOICES, unique=False)
    level = models.PositiveSmallIntegerField(default=0)


class Building(models.Model):
    planet = models.ForeignKey(
        Planet,
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=50)
    level = models.PositiveSmallIntegerField(default=0)
