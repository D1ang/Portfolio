from django import forms
from postoffice.models import Mail
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout
from crispy_forms.layout import Submit
from crispy_bootstrap5.bootstrap5 import FloatingField

from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV3


class ContactForm(forms.ModelForm):
    """
    Contact form all mails are send to
    the database.
    """
    class Meta:
        model = Mail
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'contact-form'

        # Bootstrap floating labels & extra styles
        self.helper.layout = Layout(
            FloatingField(
                'name', css_class='form-control rounded-0', wrapper_class='form-floating'
            ),
            FloatingField(
                'email', css_class='form-control rounded-0', wrapper_class='form-floating',
            ),
            FloatingField(
                'message', css_class='form-control rounded-0', wrapper_class='form-floating', style='height: 150px'
            ),
        )

        # Submit button to post
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit_form'
        self.helper.add_input(Submit('submit', 'Send your message', css_class='btn btn-send btn-lg rounded-0'))

    captcha = ReCaptchaField(
        widget=ReCaptchaV3(attrs={'required_score': 0.75}),
    )
