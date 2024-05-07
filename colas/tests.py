from django.test import TestCase
from django.urls import reverse
from .models import Cola
from .views import all_colas, product_page


class ColasViewsTestCase(TestCase):
    def setUp(self):
        """
        Setup test product.
        """
        self.product = Cola.objects.create(
            product_name='Test Cola',
            product_description='Test Description',
            price=1.99
        )

    def test_all_colas(self):
        """
        Test all products page.
        """
        response = self.client.get(reverse('colas'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'colas/all_colas.html')

    def test_product_page(self):
        """
        Test product page of an item.
        """
        response = self.client.get(reverse('product_page', args=[self.product.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'colas/product_page.html')
