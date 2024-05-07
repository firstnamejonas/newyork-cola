from django.test import TestCase
from django.urls import reverse
from .forms import NewsletterForm


class NewsletterFormTest(TestCase):
    """
    Test cases for the newsletter signup form.
    """
    def test_newsletter_form_valid_data(self):
        """
        Test newsletter signup form with valid data.
        """
        form_data = {
            'newsletter_first_name': 'John',
            'newsletter_email': 'test@example.com'
        }
        form = NewsletterForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_newsletter_form_invalid_data(self):
        """
        Test newsletter signup form with invalid data.
        """
        form = NewsletterForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 2)


class HomeViewTest(TestCase):
    """
    Test cases for the home view.
    """
    def test_home_view_status_code(self):
        """
        Test the status code of the home page.
        """
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_home_view_template(self):
        """
        Test whether the correct template is used for the home page.
        """
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'home/index.html')
