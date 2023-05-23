from django.db import models


# Create your models here.
class commodities(models.Model):
    symbol = models.CharField(max_length=200)
    date = models.DateField()
    open = models.DecimalField(max_digits=5, decimal_places=2)
    close = models.DecimalField(max_digits=5, decimal_places=2)
    volume = models.IntegerField(max_length=10)

