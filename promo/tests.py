from django.test import TestCase, Client
from django.urls import reverse
from .models import Contest
from .forms import ContestForm
from checkout.models import Order
from django.contrib.auth.models import User


class ContestPageTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_contest_page_get(self):
        """
        Test GET request for the contest page
        """
        response = self.client.get(reverse('contest_page'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'promo/contest_page.html')

    def test_contest_form_valid(self):
        """
        Test valid contest form submission
        """
        order = Order.objects.create(
            order_number='12345'
        )
        form_data = {
            'contest_username': 'testuser',
            'contest_ordernumber': '12345'
        }
        form = ContestForm(data=form_data)
        self.assertTrue(form.is_valid())
