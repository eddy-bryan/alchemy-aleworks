import uuid

from django.db import models
from django.db.models import Sum
from django.conf import settings

from inventory.models import Beer, MerchItem


class Order(models.Model):
    order_number = models.CharField(max_length=32, null=False, editable=False)
    customer_name = models.CharField(max_length=50, null=False, blank=False)
    customer_address1 = models.CharField(max_length=80, null=False, blank=False)
    customer_address2 = models.CharField(max_length=80, null=True, blank=True)
    customer_city = models.CharField(max_length=40, null=False, blank=False)
    customer_county = models.CharField(max_length=80, null=True, blank=True)
    customer_postcode = models.CharField(max_length=20, null=True, blank=True)
    customer_country = models.CharField(max_length=40, null=False, blank=False)
    customer_email = models.EmailField(max_length=254, null=False, blank=False)
    customer_phone = models.CharField(max_length=20, null=False, blank=False)
    order_date = models.DateTimeField(auto_now_add=True)
    delivery_fee = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)

    def _generate_order_number(self):
        """
        Generates a unique, random order number
        """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        self.order_total = sum(item.lineitem_total for item in self.beer_line_items.all()) + sum(item.lineitem_total for item in self.merch_line_items.all())
        if self.order_total < settings.FREE_DELIVERY_THRESHOLD:
            self.delivery_fee = settings.STANDARD_DELIVERY_COST
        else:
            self.delivery_cost = 0
        self.grand_total = self.order_total + self.delivery_cost
        self.save()


    def save(self, *args, **kwargs):
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number

class BeerLineItem(models.Model):
    order = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE, related_name='beer_line_items')
    beer = models.ForeignKey(Beer, null=False, blank=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)

    def save(self, *args, **kwargs):
        self.lineitem_total = self.beer.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Beer {self.beer.name} on order {self.order.order_number}'

class MerchLineItem(models.Model):
    order = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE, related_name='merch_line_items')
    merch_item = models.ForeignKey(MerchItem, null=False, blank=False, on_delete=models.CASCADE)
    merch_item_size = models.CharField(max_length=2, null=True, blank=True)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)

    def save(self, *args, **kwargs):
        self.lineitem_total = self.merch_item.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Merch {self.merch_item.name} on order {self.order.order_number}'