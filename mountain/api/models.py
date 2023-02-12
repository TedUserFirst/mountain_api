# -*- coding: utf-8 -*-

from django.db import models


class Peak(models.Model):
    name = models.CharField(max_length=50, unique=True, blank=False, null=False)
    latitude = models.FloatField(u"Latitude", default=0)
    longitude = models.FloatField(u"Longitude", default=0)
    altitude = models.FloatField(u"Altitude", default=0)
    
    def __str__(self):
        return self.name
