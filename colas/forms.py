from django import forms
from .models import Cola


class ProductForm(forms.ModelForm):

    class Meta:
        model = Cola
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'mb-2'
