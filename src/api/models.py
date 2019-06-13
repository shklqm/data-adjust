from django.db import models

from .constants import CHANNEL_MAX_LENGTH, COUNTRY_MAX_LENGTH, OS_MAX_LENGTH, SPEND_MAX_DECIMAL_PLACES, \
    REVENUE_MAX_DECIMAL_PLACES, SPEND_MAX_DIGITS, REVENUE_MAX_DIGITS


class Record(models.Model):
    date = models.DateField()
    channel = models.CharField(max_length=CHANNEL_MAX_LENGTH)
    country = models.CharField(max_length=COUNTRY_MAX_LENGTH)
    os = models.CharField(max_length=OS_MAX_LENGTH)
    impressions = models.IntegerField()
    clicks = models.IntegerField()
    installs = models.IntegerField()
    spend = models.DecimalField(max_digits=SPEND_MAX_DIGITS, decimal_places=SPEND_MAX_DECIMAL_PLACES)
    revenue = models.DecimalField(max_digits=REVENUE_MAX_DIGITS, decimal_places=REVENUE_MAX_DECIMAL_PLACES)