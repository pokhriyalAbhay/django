from typing import Any
from django import forms
class StudentRegistration(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    def clean(self):
        cleaned_data =  super().clean()
        valname =  self.cleaned_data['name']
        valemail =  self.cleaned_data['email']
        if len(valname)<4 :
            raise forms.ValidationError('name should be more then 4')
        if len(valemail)<4 :
            raise forms.ValidationError('email should be more then 4')
   