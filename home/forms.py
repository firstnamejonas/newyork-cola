from django import forms
from .models import NewsletterSignup


class NewsletterForm(forms.ModelForm):
    class Meta:
        model = NewsletterSignup
        fields = (
            'newsletter_first_name',
            'newsletter_email',
        )

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels.
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'newsletter_first_name': 'Your First Name',
            'newsletter_email': 'Your Email',
        }

        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'mt-3'
            self.fields[field].label = False
