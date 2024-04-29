from django.db import models


class Contest(models.Model):
    """
    Class to safe Contest Participants Data.
    """
    contest_username = models.CharField(max_length=100, null=False, blank=False)
    contest_ordernumber = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.contest_username
