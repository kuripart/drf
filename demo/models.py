from django.db import models

class Basic(models.Model):
    name = models.CharField(max_length=100)