from django import forms
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV2Checkbox
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Div
from crispy_bootstrap5.bootstrap5 import FloatingField


class ContactForm(forms.Form):
    """
    Contact form all mails are send to
    the database.
    """
    name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control rounded-0'})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control rounded-0'})
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control rounded-0', 'style': 'height: 150px'})
    )
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox(), label='')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'contact-form'

        # Bootstrap floating labels & extra styles
        self.helper.layout = Layout(
            FloatingField('name'),
            FloatingField('email'),
            FloatingField('message'),
            Div('captcha', css_class='recaptcha-container mb-3'),
        )
        # Submit button to post
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit_form'
        self.helper.add_input(Submit('submit', 'Send your message', css_class='btn btn-send btn-lg rounded-0'))
