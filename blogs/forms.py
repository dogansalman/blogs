from django import forms 
from django.forms import ModelForm

class postForm(forms.Form):
    title = forms.CharField(max_length=255, required=True)
    is_allow_comments = forms.BooleanField(required=False)
    content = forms.Textarea()
    keywords = forms.CharField(max_length=255)