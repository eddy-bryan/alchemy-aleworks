from django.contrib import admin
from .models import Beer, MerchItem


class BeerAdmin(admin.ModelAdmin):
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
