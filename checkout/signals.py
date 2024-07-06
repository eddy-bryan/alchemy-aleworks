from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import BeerLineItem, MerchLineItem


@receiver(post_save, sender=BeerLineItem)
@receiver(post_save, sender=MerchLineItem)
def update_order_on_save(sender, instance, created, **kwargs):
    instance.order.update_total()


@receiver(post_delete, sender=BeerLineItem)
@receiver(post_delete, sender=MerchLineItem)
def update_order_on_delete(sender, instance, **kwargs):
    instance.order.update_total()
