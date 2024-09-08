from django import forms
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV3


class ContactForm(forms.Form):
    contact_name = forms.CharField(
        label=(''),
        required=True,
        max_length=50,
        widget=forms.TextInput(attrs={'placeholder': 'Name'})
    )
    contact_email = forms.EmailField(
        label=(''),
        required=True,
        max_length=150,
        widget=forms.TextInput(attrs={'placeholder': 'Email'})
    )
    message = forms.CharField(
        label=(''),
        required=True,
        max_length=500,
        widget=forms.Textarea(attrs={'rows': 4, 'placeholder': 'Message'})
    )
    captcha = ReCaptchaField(
        widget=ReCaptchaV3(attrs={'required_score': 0.75}),
        label=('')
    )
