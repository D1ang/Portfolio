from django import forms


class ContactForm(forms.Form):
    contact_name = forms.CharField(
        label=('Name'),
        required=True
    )
    contact_email = forms.EmailField(
        label=('Email'),
        required=True
    )
    content = forms.CharField(
        label=('Message'),
        required=True,
        max_length=250,
        widget=forms.Textarea(attrs={'rows': 4})
    )
