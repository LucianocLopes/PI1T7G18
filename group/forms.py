from django import forms

from .models import Group, GridGroup



class GroupForm(forms.ModelForm):
    
    class Meta:
        model = Group
        fields = '__all__'


class GridGroupForm(forms.ModelForm):
    
    class Meta:
        model = GridGroup
        fields = '__all__'