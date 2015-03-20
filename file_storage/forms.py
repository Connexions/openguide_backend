from django import forms

class ImageFileForm(forms.Form):
    image = forms.ImageField(
        label = 'Select an image'
    )
