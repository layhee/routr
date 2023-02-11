from django.db import models
from django.urls import reverse

# gear_item = (
#     ('bag', 'for carrying my camp stove', '2 liter', 'Spindle', True),
#     ('stove', 'for cooking my meals', 'mini', 'Snow Peak', True),
#     ('tent', 'for sleeping in', '3 person', 'Big Agnes', 'Tiger Wall UL3', True),
# )


class Gear(models.Model):
    name = models.CharField(max_length=100)
    use = models.CharField(max_length=100)
    size = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    necessary = models.CharField(max_length=100)
    # trip = models.ForeignKey(
    #     Trip, on_delete=models.CASCADE, related_name='gears', default=None)

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

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("detail", kwargs={"trip_id": self.id})
