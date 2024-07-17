from django.test import SimpleTestCase

from .forms import CustomerProfileForm


class CustomerProfileFormTests(SimpleTestCase):
    """
    Test suite for the customer profile form.

    These tests verify the behavior of the add beer form.
    """

    def test_customer_profile_form_valid(self):
        """Test whether the customer profile form is valid with valid data."""
        form_data = {
            'default_customer_address1': 'test',
            'default_customer_address2': 'test',
            'default_customer_city': 'test',
            'default_customer_county': 'test',
            'default_customer_postcode': 'TE57ST',
            'default_customer_phone': '12345678901'
        }
        form = CustomerProfileForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_customer_profile_form_invalid(self):
        """
        Test whether the customer profile form is invalid with invalid data.
        """
        form_data = {
            'default_customer_postcode': '123456789012345678901',
            'default_customer_phone': '123456789012345678901'
        }
        form = CustomerProfileForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_customer_profile_form_fields(self):
        """Test whether the CustomerProfileForm has the expected fields."""
        form = CustomerProfileForm()
        self.assertTrue('default_customer_address1' in form.fields)
        self.assertTrue('default_customer_address2' in form.fields)
        self.assertTrue('default_customer_city' in form.fields)
        self.assertTrue('default_customer_county' in form.fields)
        self.assertTrue('default_customer_postcode' in form.fields)
        self.assertTrue('default_customer_phone' in form.fields)
