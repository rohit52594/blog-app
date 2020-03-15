from django import forms

class RegisterForm(forms.Form):

    name = forms.CharField(max_length = 100,
        widget = forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": 'Enter your name'
        })
    )

    email = forms.CharField(max_length = 100,
        widget = forms.EmailInput(
            attrs = {
                'class': 'form-control',
                'placeholder': 'Enter your email address'
            }
        )
    )

    phone = forms.CharField(max_length = 100,
        widget = forms.NumberInput(
            attrs = {
                'class': 'form-control',
                'placeholder': 'Enter your contact number'
            }
        )
    )

    password = forms.CharField(max_length = 100,
        widget = forms.PasswordInput(
            attrs = {
                'class': 'form-control',
                'placeholder': 'Enter a secure password'
            }
        )
    )