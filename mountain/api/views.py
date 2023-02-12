# -*- coding: utf-8 -*-

from rest_framework import viewsets, generics
from . import serializers
from . import models as api_models


class PeakViewSet(viewsets.ModelViewSet):
    queryset = api_models.Peak.objects.all()
    serializer_class = serializers.PeakSerializer


class PeakListInBoundingBox(generics.ListAPIView):
    serializer_class = serializers.PeakSerializer

    def get_queryset(self):
        min_latitude = self.kwargs['min_latitude']
        min_longitude = self.kwargs['min_longitude']
        max_latitude = self.kwargs['max_latitude']
        max_longitude = self.kwargs['max_longitude']

        queryset = api_models.Peak.objects.filter(latitude__gte=min_latitude, latitude__lte=max_latitude,
                                                  longitude__gte=min_longitude, longitude__lte=max_longitude)

        print(queryset)
        return queryset
