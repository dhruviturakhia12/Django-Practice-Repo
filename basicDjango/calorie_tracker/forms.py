from django.forms import ModelForm
from .models import Food


class CreatePollForm(ModelForm):
    class Meta:
        model = Food
        fields = ["item", "carbohydrates", "proteins", "fats", "calories"]
