from django import forms
from .models import Task
class Task_Form(forms.ModelForm):
    class Meta:
        model = Task
        fields=['title','description']
