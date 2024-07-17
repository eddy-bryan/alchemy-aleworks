from django import forms
from .models import CustomerProfile


class CustomerProfileForm(forms.ModelForm):
    """
    Form for updating customer profile information.

    This form is based on the CustomerProfile model, excluding the 'customer'
    field. It provides placeholders and custom attributes for form fields.

    Attributes:
        placeholders (dict): Dictionary mapping field names to placeholder
                             text.
    """
    class Meta:
        model = CustomerProfile
        exclude = ('customer',)

    def __init__(self, *args, **kwargs):
        """
        Initialise the CustomerProfileForm instance.

        Sets autofocus on the 'default_customer_phone' field, adds
        placeholders, and applies custom CSS classes to form inputs.

        Args:
            *args: Positional arguments passed to the form.
            **kwargs: Keyword arguments passed to the form.
        """
        super().__init__(*args, **kwargs)

        # Define placeholders for form fields
        placeholders = {
            'default_customer_phone': 'Customer Phone',
            'default_customer_postcode': 'Customer Postcode',
            'default_customer_city': 'Customer City',
            'default_customer_address1': 'Customer Address 1',
            'default_customer_address2': 'Customer Address 2',
            'default_customer_county': 'Customer County',
        }

        # Set autofocus on default_customer_phone field
        self.fields['default_customer_phone'].widget.attrs['autofocus'] = True

        # Assign placeholders and CSS classes to form fields
        for field in self.fields:
            if field != 'default_customer_country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'profile-form-input'
            self.fields[field].label = False
