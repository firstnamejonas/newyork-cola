from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Order, OrderLineItem
from .views import checkout, checkout_success
from colas.models import Cola


class CheckoutViewsTestCase(TestCase):
    def setUp(self):
        """
        Setup testuser and test product.
        """
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.product = Cola.objects.create(
            product_name='Test Cola',
            product_description='Test Description',
            price=1.99
        )

    def test_checkout(self):
        """
        Tests checkout view.
        """
        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('checkout'))
        self.assertEqual(response.status_code, 302)
        # If nothing is in the bag, user gets redirected to product page
        self.assertEqual(response.url, '/products/')

    def test_checkout_success(self):
        """
        Tests checkout success view.
        """
        order = Order.objects.create(
            user_profile=self.user.userprofile,
            full_name='Test User',
            email='test@example.com',
            country='US',
            postcode='12345',
            town_or_city='Test City',
            street_address1='Test Street',
            order_total=1.99
        )
        response = self.client.get(reverse('checkout_success', args=[order.order_number]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout/checkout_success.html')
