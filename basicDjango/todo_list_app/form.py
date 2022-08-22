from django.forms import ModelForm
from .models import todo_list_app


class CreateToDoForm(ModelForm):
    class Meta:
        model = todo_list_app
        fields = ["task","roles","due_date"]