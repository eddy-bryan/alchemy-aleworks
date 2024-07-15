from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    """
    Form representing an order for customer details.

    Inherits from Django's ModelForm to automatically generate form fields
    based on the Order model.

    Attributes:
        Meta: Specifies the model (Order) and fields to include in the form.

    Methods:
        __init__: Initialises the form with placeholders, autofocus, and CSS classes for styling.
    """
    class Meta:
        model = Order
        fields = ('customer_name', 'customer_email', 'customer_phone',
                  'customer_address1', 'customer_address2',
                  'customer_city', 'customer_postcode', 'customer_country',
                  'customer_county',)

    def __init__(self, *args, **kwargs):
        """
        Initialises the form with customizations:
        - Sets placeholders for input fields.
        - Autofocuses on the customer name field.
        - Adds CSS class for styling uniformity.
        """
        super().__init__(*args, **kwargs)
        
        # Placeholder texts for each field
        placeholders = {
            'customer_name': 'Customer Name',
            'customer_email': 'Customer Email',
            'customer_phone': 'Customer Phone',
            'customer_postcode': 'Customer Postcode',
            'customer_city': 'Customer City',
            'customer_address1': 'Customer Address 1',
            'customer_address2': 'Customer Address 2',
            'customer_county': 'Customer County',
        }

        # Autofocus on the customer name field
        self.fields['customer_name'].widget.attrs['autofocus'] = True
        
        # Iterate through each form field to set attributes
        for field in self.fields:
            # Exclude 'customer_country' from placeholder customisation
            if field != 'customer_country':
                # Customise placeholder based on field requirement
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            
            # Add a CSS class for styling consistency
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            
            # Disable default labels for fields
            self.fields[field].label = False
