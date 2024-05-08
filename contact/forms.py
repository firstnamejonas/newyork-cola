from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = (
            'contact_full_name',
            'contact_email',
            'contact_ordernumber',
            'contact_issue',
            'contact_message',
        )

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'contact_full_name': 'Your Full Name',
            'contact_email': 'Your Email',
            'contact_ordernumber': 'Your Ordernumber (optional)',
            'contact_issue': None,
            'contact_message': 'Your message for us....',
        }

        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'mt-3'
            self.fields[field].label = False

            # Assign custom classes for 'contact_issue' field
            if field == 'contact_issue':
                self.fields[field].widget.attrs['class'] += ' form-select'
