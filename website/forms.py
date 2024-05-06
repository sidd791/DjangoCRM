from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Record

class SignUp(UserCreationForm):
    email = forms.EmailField(label = '', widget = forms.TextInput(attrs = {'class':'form-control', 'placeholder':'Email'}))
    first_name = forms.CharField(label = '', max_length = 100, widget = forms.TextInput(attrs = {'class':'form-control', 'placeholder': 'First Name'}))
    last_name = forms.CharField(label = '', max_length = 100, widget = forms.TextInput(attrs =  {'class':'form-control', 'placeholder': 'Last Name'}))


    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password1', 'password2']

class AddForm(forms.ModelForm):
    first_name = forms.CharField( required=True,label = '', max_length = 100, widget = forms.TextInput(attrs = {'class':'form-control', 'placeholder': 'First Name'}))
    last_name = forms.CharField(required=True, label = '', max_length = 100, widget = forms.TextInput(attrs =  {'class':'form-control', 'placeholder': 'Last Name'}))
    email = forms.EmailField(required=True, label = '', widget = forms.TextInput(attrs = {'class':'form-control', 'placeholder':'Email'}))
    ph_num = forms.CharField(required=True, label = '', widget = forms.TextInput(attrs = {'class':'form-control', 'placeholder':'Ph Num'}))
    address = forms.CharField(required=True, label = '', widget = forms.TextInput(attrs = {'class':'form-control', 'placeholder':'Address'}))
    city = forms.CharField(required=True, label = '', widget = forms.TextInput(attrs = {'class':'form-control', 'placeholder':'City'}))
    state = forms.CharField(required=True, label = '', widget = forms.TextInput(attrs = {'class':'form-control', 'placeholder':'State'}))
    zipcode = forms.CharField(required=True, label = '', widget = forms.TextInput(attrs = {'class':'form-control', 'placeholder':'Zipcode'}))

    class Meta:
        model = Record
        exclude = ("user",)
