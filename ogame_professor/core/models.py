from django.db import models

# Create your models here.


class Planet(models.Model):
    name = models.CharField(max_length=50)
    temperature = models.IntegerField()

    def __str__(self) -> str:
        return self.name


class MetalMine(models.Model):
    planet = models.ForeignKey(Planet, on_delete=models.CASCADE)
    base_output = 30

    def __str__(self) -> str:
        return self.planet.name
