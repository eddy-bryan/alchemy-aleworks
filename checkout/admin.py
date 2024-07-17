from django.contrib import admin
from .models import Order, BeerLineItem, MerchLineItem


class BeerLineItemAdminInline(admin.TabularInline):
    """
    Admin inline representation for BeerLineItem model.

    This inline allows editing BeerLineItem objects within the OrderAdmin page
    in the Django admin interface.

    Attributes:
        model: Specifies the model to be used for the inline (BeerLineItem).
        readonly_fields: Specifies which fields should be read-only in the
        admin interface (lineitem_total).
    """
    model = BeerLineItem
    readonly_fields = ('lineitem_total',)


class MerchLineItemAdminInline(admin.TabularInline):
    """
    Admin inline representation for MerchLineItem model.

    This inline allows editing MerchLineItem objects within the OrderAdmin page
    in the Django admin interface.

    Attributes:
        model: Specifies the model to be used for the inline (MerchLineItem).
        readonly_fields: Specifies which fields should be read-only in the
        admin interface (lineitem_total).
    """
    model = MerchLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    """
    Admin representation for Order model.

    This class defines how the Order model is presented in the Django admin
    interface, including inlines, readonly fields, displayed fields, list
    display, and ordering.

    Attributes:
        model: Specifies the model to be represented (Order).
        inlines: Specifies the inline models to be displayed with the Order
        model (BeerLineItemAdminInline, MerchLineItemAdminInline).
        readonly_fields: Specifies which fields should be read-only in the
                         admin interface.
        fields: Specifies the fields to be displayed and their order in the
                edit view of the admin interface.
        list_display: Specifies which fields to display in the list view of
                      the admin interface.
        ordering: Specifies the default ordering of records in the admin
                  interface list view.
    """
    model = Order
    inlines = (BeerLineItemAdminInline, MerchLineItemAdminInline,)
    readonly_fields = ('order_number', 'order_date', 'delivery_fee',
                       'order_total', 'grand_total', 'original_bag',
                       'stripe_pid',)
    fields = ('order_number', 'customer_profile', 'order_date',
              'customer_name', 'customer_email', 'customer_phone',
              'customer_address1', 'customer_address2', 'customer_city',
              'customer_county', 'customer_postcode', 'customer_country',
              'delivery_fee', 'order_total', 'grand_total', 'original_bag',
              'stripe_pid',)
    list_display = ('order_number', 'order_date', 'customer_name',
                    'order_total', 'delivery_fee', 'grand_total',)
    ordering = ('-order_date',)


admin.site.register(Order, OrderAdmin)
