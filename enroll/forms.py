
from django import forms
class studentregistration(forms.Form):
  first_name=forms.CharField()
  last_name=forms.CharField()
  email=forms.EmailField()
  password=forms.CharField(widget=forms.PasswordInput)