from django.db import models


class Earthquakes(models.Model):
    date = models.CharField()
    time = models.CharField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    depth = models.FloatField()
    magnitude = models.FloatField()

    def __str__(self):
        return self.magnitude
