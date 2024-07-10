from django.contrib import admin
from .models import Order, BeerLineItem, MerchLineItem


class BeerLineItemAdminInline(admin.TabularInline):
    model = BeerLineItem
    readonly_fields = ('lineitem_total',)


class MerchLineItemAdminInline(admin.TabularInline):
    model = MerchLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    model = Order
    inlines = (BeerLineItemAdminInline, MerchLineItemAdminInline,)
    readonly_fields = ('order_number', 'order_date', 'delivery_fee', 'order_total', 'grand_total', 'original_bag', 'stripe_pid',)
    fields = ('order_number', 'customer_profile', 'order_date', 'customer_name', 'customer_email', 'customer_phone',
              'customer_address1', 'customer_address2', 'customer_city', 'customer_county',
              'customer_postcode', 'customer_country', 'delivery_fee', 'order_total', 'grand_total', 'original_bag', 'stripe_pid',)
    list_display = ('order_number', 'order_date', 'customer_name', 'order_total', 'delivery_fee', 'grand_total',)
    ordering = ('-order_date',)


admin.site.register(Order, OrderAdmin)