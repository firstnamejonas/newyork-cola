from django.test import TestCase
from django.urls import reverse
from .models import Contact
from .forms import ContactForm


class ContactFormTest(TestCase):
    """
    Test contact app forms.
    """
    def test_contact_form_valid_data(self):
        form = ContactForm(data={
            'contact_full_name': 'John Doe',
            'contact_email': 'test@example.com',
            'contact_issue': 'order',
            'contact_message': 'Test Message'
        })
        self.assertTrue(form.is_valid())

    def test_contact_form_invalid_data(self):
        form = ContactForm(data={})
        self.assertFalse(form.is_valid())


class ContactViewTest(TestCase):
    """
    Test contact app views.
    """
    def test_contact_page_view(self):
        response = self.client.get(reverse('contact_page'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact/contact_page.html')
