from django.db import models
from cloudinary.models import CloudinaryField


class Cola(models.Model):
    """
    Models to store product data.
    """
    product_name = models.CharField(
        max_length=100,
        null=False,
        blank=False
    )
    product_description = models.TextField(
        max_length=500,
        null=False,
        blank=False
    )
    price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=False,
        blank=False
    )
    product_image = CloudinaryField(
        'image',
        null=False,
        blank=False
    )
    ingredients = models.TextField(
        max_length=500,
        null=True,
        blank=True
    )
    nutrition_facts = models.TextField(
        max_length=500,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.product_name
