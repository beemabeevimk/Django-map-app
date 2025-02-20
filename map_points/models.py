from django.contrib.gis.db import models

# Create your models here.

class MapPoints(models.Model):
    CATEGORY_CHOICES = [
        ('park','Park'),
        ('restaurant','Restaurant'),
        ('museum','Museum'),
    ]

    title = models.CharField(max_length=200)
    category = models.CharField(max_length=60,choices=CATEGORY_CHOICES)
    icon = models.CharField(max_length=255, default='fas fa-map-marker-alt')
    # latitude = models.FloatField()
    # longitude = models.FloatField()
    location = models.PointField()
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)

    def __str__(self):
        return self.title