from django.db import models


class Earthquakes(models.Model):
    datetime = models.CharField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    depth = models.IntegerField()
    magnitude = models.FloatField()

    def __str__(self):
        return self.magnitude
