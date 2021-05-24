from django.db import models


# Create your models here.


class Country(models.Model):
    name = models.CharField(max_length=255)
    capital = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField()
    surface = models.FloatField()
    population = models.FloatField()
    historique = models.TextField()
    ressources = models.TextField()
    personnalités = models.TextField()
    drapeau = models.ImageField(upload_to='media')
    drapeau_carre = models.ImageField(upload_to='media', blank=True, null=True)
    hymne = models.FileField(upload_to='media')


class SlideShowImages(models.Model):
    image = models.ImageField(upload_to='slideShow')
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)


class Person(models.Model):
    name = models.CharField(max_length=255)
    fonction = models.CharField(max_length=255)
    image = models.ImageField(upload_to='slideShow')
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True)


class Vedios(models.Model):
    vedio = models.FileField(upload_to='vedios')
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True)
