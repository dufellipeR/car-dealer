from django.db import models


class Car(models.Model):
    make = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    price = models.FloatField()
    odometer = models.PositiveIntegerField()
    transmission = models.CharField()


class User(models.Model):
    pass
