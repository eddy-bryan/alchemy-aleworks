from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('customer_name', 'customer_email', 'customer_phone',
                  'customer_address1', 'customer_address2',
                  'customer_city', 'customer_postcode', 'customer_country',
                  'customer_county',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'customer_name': 'Full Name',
            'customer_email': 'Email Address',
            'customer_phone': 'Phone Number',
            'customer_country': 'Country',
            'customer_postcode': 'Postal Code',
            'customer_city': 'Town or City',
            'customer_address1': 'Street Address 1',
            'customer_address2': 'Street Address 2',
            'customer_county': 'County',
        }

        self.fields['customer_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False
