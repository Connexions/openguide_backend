from django import forms

class ImageFileForm(forms.Form):
    file = forms.ImageField(
        label = 'Select an image'
    )
