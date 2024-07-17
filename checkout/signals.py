from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import BeerLineItem, MerchLineItem


@receiver(post_save, sender=BeerLineItem)
@receiver(post_save, sender=MerchLineItem)
def update_order_on_save(sender, instance, created, **kwargs):
    """
    Signal receiver function to update order total on save of BeerLineItem or
    MerchLineItem.

    When a BeerLineItem or MerchLineItem is saved (created or updated),
    this function updates the total for the associated order.
    """
    instance.order.update_total()


@receiver(post_delete, sender=BeerLineItem)
@receiver(post_delete, sender=MerchLineItem)
def update_order_on_delete(sender, instance, **kwargs):
    """
    Signal receiver function to update order total on deletion of BeerLineItem
    or MerchLineItem.

    When a BeerLineItem or MerchLineItem is deleted,
    this function updates the total for the associated order.
    """
    instance.order.update_total()
