from django.db import models


class NewsletterSignup(models.Model):
    """
    Class to safe newsletter form data.
    """

    newsletter_first_name = models.CharField(max_length=100, null=False, blank=False)
    newsletter_email = models.EmailField(max_length=254, null=False, blank=False)

    def __str__(self):
        return self.newsletter_first_name
