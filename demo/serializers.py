from rest_framework import serializers
from . import models


class BasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Basic
        fields = ('id', 'name')