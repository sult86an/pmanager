from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from initiatives.models import Initi, Goals
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.contrib.auth.validators import ASCIIUsernameValidator


class GoalsForm(forms.ModelForm):

    class Meta:
        model = Goals
        fields = ['mub', 'goal']
        labels = {
            "mub": "اسم المبادرة ",
            "goal": "الهدف"
            }
