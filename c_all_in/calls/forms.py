from django import forms

class AnnounceForm(forms.Form):
    filename = forms.FileField()