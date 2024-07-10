from django import forms
from .models import CustomerProfile


class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model = CustomerProfile
        exclude = ('customer',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'default_customer_phone': 'Customer Phone',
            'default_customer_postcode': 'Customer Postcode',
            'default_customer_city': 'Customer City',
            'default_customer_address1': 'Customer Address 1',
            'default_customer_address2': 'Customer Address 2',
            'default_customer_county': 'Customer County',
        }

        self.fields['default_customer_phone'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'default_customer_country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'profile-form-input'
            self.fields[field].label = False
