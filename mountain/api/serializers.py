from rest_framework import serializers

from . import models as api_models

class PeakSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = api_models.Peak
        fields = ('__all__')
