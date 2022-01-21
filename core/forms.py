from socket import fromshare
from django import forms
from .models import Links

class FormLinks(forms.ModelForm):
    class Meta:
        model = Links
        fields = "__all__"