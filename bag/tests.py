from django.test import TestCase
from django.urls import reverse
from django.contrib.messages import get_messages
from django.contrib.auth.models import User
from colas.models import Cola
from .views import view_bag, add_items, adjust_bag, delete_items


class BagViewsTestCase(TestCase):
    """
    Sets up the environment for the tests by creating
    a test user and a test product.
    """
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.product = Cola.objects.create(
            product_name='Test Cola',
            product_description='Test Description',
            price=1.99
        )

    def test_view_bag(self):
        """
        Tests view_bag view
        """
        response = self.client.get(reverse('view_bag'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bag/bag.html')

    def test_add_items(self):
        """
        Tests add item to shopping bag view
        """
        self.client.login(username='testuser', password='12345')
        response = self.client.post(reverse('add_items', args=[self.product.pk]), {'quantity': 1, 'redirect_url': '/'})
        self.assertEqual(response.status_code, 302)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), f'Test Cola successfully added to your shopping bag!')

    def test_adjust_bag_quantity(self):
        """
        Tests adjusting the quantity of an item in the shopping bag
        """
        self.client.login(username='testuser', password='12345')
        # Adding an item to the bag
        response_add = self.client.post(reverse('add_items', args=[self.product.pk]), {'quantity': 1, 'redirect_url': '/'})
        self.assertEqual(response_add.status_code, 302)
        # Adjusting the quantity of the added item
        response_adjust = self.client.post(reverse('adjust_bag', args=[self.product.pk]), {'quantity': 2})
        self.assertEqual(response_adjust.status_code, 302)
        # Verifying the adjusted quantity
        bag = self.client.session.get('bag')
        self.assertEqual(bag[str(self.product.pk)], 2)
        # Verifying the success message
        messages = list(get_messages(response_adjust.wsgi_request))
        self.assertEqual(len(messages), 2)  # Adjusted quantity message + success message
        self.assertEqual(str(messages[1]), f'Test Cola quantity has been updated!')

    def test_delete_items(self):
        """
        Tests deleting items from the shopping bag
        """
        # Add Test Product
        product = Cola.objects.create(
            product_name='Test Cola',
            product_description='Test Description',
            price=1.99
        )
        
        # Add item to bag
        self.client.login(username='testuser', password='12345')
        response_add = self.client.post(reverse('add_items', args=[product.pk]), {'quantity': 1, 'redirect_url': '/'})
        self.assertEqual(response_add.status_code, 302)
        
        # Delete item from bag
        response_delete = self.client.post(reverse('delete_items', args=[product.pk]))
        self.assertEqual(response_delete.status_code, 200)
