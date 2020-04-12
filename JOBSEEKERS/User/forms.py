from django.forms import ModelForm
from .models import Profile
from django import forms

class DateInput(forms.DateInput):
    input_type = 'Date'
    format = '%m/%d/%Y'
    input_formats = '%m/%d/%Y'


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['contact' , 'gender' , 'birth_date' , 'skils' , 'resume' , 'img' , 'exprerience_type' , 'street_name' , 'city' , 'states']

        widgets = {
            'contact': forms.TextInput(attrs={'placeholder': '+91 11111 11111', 'class': 'form-control'}),
            'birth_date': forms.DateInput(attrs={'placeholder': 'YYYY-MM-DD', 'class': 'form-control'}),
            'skils': forms.Textarea(attrs={'placeholder': 'Enter your skils', 'class': 'form-control'}),
            'resume': forms.FileInput(attrs={'placeholder': '', 'class': 'form-control'}),
            'img': forms.FileInput(attrs={'placeholder': '', 'class': 'form-control'}),
            'street_name': forms.TextInput(attrs={'placeholder': 'street name', 'class': 'form-control'}),


        }

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['contact'].label = ''
        self.fields['gender'].label = ''
        self.fields['birth_date'].label = ''
        self.fields['skils'].label = ''
        self.fields['resume'].label = ''
        self.fields['img'].label = ''
        self.fields['exprerience_type'].label = ''
        self.fields['street_name'].label = ''
        self.fields['city'].label = ''
        self.fields['states'].label = ''

