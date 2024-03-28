from django import forms

from .models import Task

class Taskform(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            "task"
        ]
        widgets = {
            "task": forms.TextInput(attrs={'style': ' border-radius: 10px;background-color: rgb(118, 145, 136); height:50px; border:None; '}),
        }