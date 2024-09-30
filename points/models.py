from django.db import models

class Points(models.Model):
    payer = models.CharField(max_length=50)
    points = models.IntegerField()
    timestamp = models.DateTimeField()
