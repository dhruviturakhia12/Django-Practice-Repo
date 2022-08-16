from django.db import models


class Destination(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField()
    img = models.ImageField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)
    number = models.IntegerField()
