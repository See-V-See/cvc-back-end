from django.db import models
from django import forms
from .models import ImgTable

class PostForm(forms.ModelForm):
    class Meta:
        model = ImgTable
        fields = ['image']
