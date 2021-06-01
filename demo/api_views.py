from rest_framework import viewsets
from . import models
from . import serializers


class BasicViewset(viewsets.ModelViewSet):
    queryset = models.Basic.objects.all()
    serializer_class = serializers.BasicSerializer