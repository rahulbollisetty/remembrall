from django import forms
from django.forms import ModelForm,TextInput
from .models import PhoneNumber

class PhoneNumberForm(ModelForm):
    class Meta:
        model = PhoneNumber
        fields = ('phn_no',)
        widgets = {
            'phn_no' : TextInput(attrs={'placeholder':'Enter Your Phone Number','maxlength':12}
            )}