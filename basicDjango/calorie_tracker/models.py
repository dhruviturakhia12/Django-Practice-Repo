from django.db import models
from django.contrib.auth.models import User


class Food(models.Model):
    item = models.CharField(max_length=100)
    carbohydrates = models.FloatField()
    proteins = models.FloatField()
    fats = models.FloatField()
    calories = models.FloatField()

    def __str__(self):
        return self.item


class CalorieConsume(models.Model):
    food_consumed = models.ForeignKey(Food, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
