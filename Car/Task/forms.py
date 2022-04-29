from django import forms
from .models import carlist, Show_room

class carlistForm(forms.ModelForm):
    class Meta:
        model=carlist
        fields='__all__'

class Show_roomForm(forms.ModelForm):
    class Meta:
        model=Show_room
        fields='__all__'