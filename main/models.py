from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User


class Gear(models.Model):
    name = models.CharField(max_length=100)
    use = models.CharField(max_length=100)
    size = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    necessary = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("gear_detail", kwargs={"gear_id": self.id})


class Trip(models.Model):
    name = models.CharField(max_length=100)
    mode = models.CharField(max_length=100)
    distance = models.IntegerField()
    nights = models.IntegerField()
    start = models.CharField(max_length=100)
    end = models.CharField(max_length=250)
    gear = models.ManyToManyField(Gear)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("detail", kwargs={"trip_id": self.id})
