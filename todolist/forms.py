from django import forms
from django.forms import DateTimeInput
from todolist.models import Task


class TaskCreateForm(forms.ModelForm):
    deadline = forms.DateTimeField(required=False, widget=DateTimeInput(attrs={'type': 'datetime-local'}))

    class Meta:
        model = Task
        fields = "__all__"
