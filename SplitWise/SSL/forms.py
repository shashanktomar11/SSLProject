from django import forms
from .models import *
from django.forms import ModelChoiceField

class NameForm(forms.Form):
    your_name = forms.CharField(label="Friend's username", max_length=100)

class GroupForm(forms.Form):
    group_name = forms.CharField(label='Group name', max_length=100)
    friends = forms.ModelMultipleChoiceField(queryset=Friend.objects.all(),initial=0)