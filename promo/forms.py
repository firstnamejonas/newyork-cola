from django import forms
from .models import Contest


class ContestForm(forms.ModelForm):
    class Meta:
        model = Contest
        fields = ('contest_username', 'contest_ordernumber')

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'contest_username': 'Your Username',
            'contest_ordernumber': 'Your Ordernumber',
        }

        self.fields['contest_username'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'mt-3'
            self.fields[field].label = False
