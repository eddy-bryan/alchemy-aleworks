from django.contrib import admin
from .models import Beer, MerchItem


class BeerAdmin(admin.ModelAdmin):
    """
    Admin configuration for Beer model.

    This class defines how the Beer model is displayed and interacted with
    in the Django admin interface. It specifies the fields to display in the
    list view and their ordering.

    Attributes:
        list_display: Tuple of fields to display as columns in the admin list
                      view.
        ordering: Tuple specifying the default sorting order for Beer objects.
    """
    list_display = (
        'sku',
        'name',
        'type',
        'alcohol_content',
        'price',
        'limited_edition',
        'image',
    )

    ordering = ('sku',)


class MerchItemAdmin(admin.ModelAdmin):
    """
    Admin configuration for MerchItem model.

    This class defines how the MerchItem model is displayed and interacted with
    in the Django admin interface. It specifies the fields to display in the
    list view and their ordering.

    Attributes:
        list_display: Tuple of fields to display as columns in the admin list
                      view.
        ordering: Tuple specifying the default sorting order for MerchItem
                  objects.
    """
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'sized_item',
        'image',
    )

    ordering = ('sku',)


admin.site.register(Beer, BeerAdmin)
admin.site.register(MerchItem, MerchItemAdmin)
