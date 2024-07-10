from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from django_countries.fields import CountryField


class CustomerProfile(models.Model):
    """
    A user profile model for maintaining default
    delivery information and order history
    """
    customer = models.OneToOneField(User, on_delete=models.CASCADE)
    default_customer_address1 = models.CharField(max_length=80, null=True, blank=True)
    default_customer_address2 = models.CharField(max_length=80, null=True, blank=True)
    default_customer_city = models.CharField(max_length=40, null=True, blank=True)
    default_customer_county = models.CharField(max_length=80, null=True, blank=True)
    default_customer_postcode = models.CharField(max_length=20, null=True, blank=True)
    default_customer_country = CountryField(blank_label='Country', null=True, blank=True)
    default_customer_phone = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.customer.username


@receiver(post_save, sender=User)
def create_or_update_customer_profile(sender, instance, created, **kwargs):
    """
    Create or update the user profile
    """
    if created:
        CustomerProfile.objects.create(customer=instance)
    else:
        instance.customerprofile.save()