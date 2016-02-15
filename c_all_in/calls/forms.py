from django import forms

class AnnounceForm(forms.Form):
    # The POST field for the file is called 'filename' even though it contains
    # the file itself. It should really be called just 'file'.
    filename = forms.FileField()