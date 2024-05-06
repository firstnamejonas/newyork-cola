from django.db import models

CONTACT_CHOICES = (
    ('choices', 'Choose an Issue (optional)'),
    ('order', 'Something is wrong with my Order.'),
    ('collaboration', 'I / We want to collaborate with NEW YORK COLA.'),
    ('product', 'I have a question about the product.'),
)


class Contact(models.Model):
    """
    Class to save contact form data.
    """

    contact_full_name = models.CharField(
        max_length=100,
        null=False,
        blank=False
    )
    contact_email = models.EmailField(
        max_length=254,
        null=False,
        blank=False
    )
    contact_ordernumber = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )
    contact_issue = models.CharField(
        max_length=100,
        choices=CONTACT_CHOICES,
        default='choices'
    )
    contact_message = models.TextField(
        max_length=500,
        null=False,
        blank=False
    )

    def __str__(self):
        return self.contact_full_name
