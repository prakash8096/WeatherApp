from django import forms

class AddcityForm(forms.Form):
    city=forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'class':"form-control",
                'placeholder':"Add City"
                

            }
        )
    )