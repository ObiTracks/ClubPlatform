from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
  
  
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()
  
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

    def save(self, commit=True):
        user = super(UserRegisterForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
  
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
  
    class Meta:
        model = User
        fields = ['username', 'email']
  
  
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"