from django import forms

class AnnounceForm(forms.Form):
    filename = forms.FileField(upload_to='announce_uploads')