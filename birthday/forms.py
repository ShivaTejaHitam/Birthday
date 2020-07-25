
from django import forms
from . import models

class MemoriesForm(forms.Form):
    title=forms.CharField()
    image=forms.FileField()

class VideosForm(forms.Form):
    title=forms.CharField()
    video=forms.FileField()

class StoriesForm(forms.Form):
    title=forms.CharField()
    Story=forms.CharField()

class UserForm(forms.Form):
    email=forms.CharField()
    password=forms.CharField()