from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, userPreferences, car, carDetails



class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('company', 'email_confirmed')

class userPreferencesForm(forms.ModelForm):
    class Meta:
        model = userPreferences
        fields = ('humidity', 'temperature', 'displayStartPage', 'radioWave', 'tvChannel', 'frigeTemperature')

class car(forms.ModelForm):
    class Meta:
        model = car
        fields = ('mark', 'model', 'city', 'county', 'location')

class carDetails(forms.ModelForm):
    class Meta:
        model = carDetails
        fields = ('radio', 'display', 'airConditioner', 'glassFogging', 'inside', 'price', 'lights', 'colour', 'car')