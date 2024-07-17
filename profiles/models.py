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
    customer = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    default_customer_address1 = models.CharField(
        max_length=80,
        null=True,
        blank=True
    )
    default_customer_address2 = models.CharField(
        max_length=80,
        null=True,
        blank=True
    )
    default_customer_city = models.CharField(
        max_length=40,
        null=True,
        blank=True
    )
    default_customer_county = models.CharField(
        max_length=80,
        null=True,
        blank=True
    )
    default_customer_postcode = models.CharField(
        max_length=20,
        null=True,
        blank=True
    )
    default_customer_country = CountryField(
        blank_label='Country',
        null=True,
        blank=True
    )
    default_customer_phone = models.CharField(
        max_length=20,
        null=True,
        blank=True
    )

    def __str__(self):
        """
        String representation of the CustomerProfile instance.

        Returns:
            str: Username of the associated User instance.
        """
        return self.customer.username


@receiver(post_save, sender=User)
def create_or_update_customer_profile(sender, instance, created, **kwargs):
    """
    Create or update the user profile.

    This function is connected to the post_save signal of the User model.
    When a new User instance is created, a corresponding CustomerProfile
    instance is created. If an existing User instance is saved (updated),
    the associated CustomerProfile instance is updated.

    Args:
        sender (type): The model class that sent the signal (User in this
        case). instance (User): The actual instance of the User model that
        was saved. created (bool): Boolean indicating if a new instance was
        created.

    Keyword Args:
        **kwargs: Additional keyword arguments passed by the signal.
    """
    if created:
        CustomerProfile.objects.create(customer=instance)
    else:
        instance.customerprofile.save()
