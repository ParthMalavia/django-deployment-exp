from django import forms
from django.core import validators
from django.contrib.auth.models import User
from first_app.models import UserM, UserProfileInfo


class UserForm2(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    
    class Meta():
        model = User
        fields = ("username", "email", "password")


class UserProfileInfoForm(forms.ModelForm):
    
    class Meta:
        model = UserProfileInfo
        fields = ("portfolio_site", "prifile_pic")


class UserForm(forms.ModelForm):

    class Meta:
        model = UserM
        fields = '__all__'


def check_for_z(value):
    if value[0].lower() != 'z':
        raise forms.ValidationError("Needs to start with 'z'.")


class FormName(forms.Form):
    name = forms.CharField(validators=[check_for_z])
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField(required=False,
                                 widget=forms.HiddenInput,
                                 validators=[validators.MaxLengthValidator(0)])

    def clean_botcatcher(self):
        botcatcher = self.cleaned_data['botcatcher']
        if len(botcatcher) > 0:
            raise forms.ValidationError("GOTCHA BOT!!")
        return botcatcher

