from django.test import SimpleTestCase

from .forms import OrderForm


class OrderFormTests(SimpleTestCase):
    """
    Test suite for the order form.

    These tests verify the behavior of the add beer form.
    """
    def test_order_form_fields(self):
        """Test whether the OrderForm has the expected fields."""
        form = OrderForm()
        self.assertTrue('customer_address1' in form.fields)
        self.assertTrue('customer_address2' in form.fields)
        self.assertTrue('customer_city' in form.fields)
        self.assertTrue('customer_county' in form.fields)
        self.assertTrue('customer_postcode' in form.fields)
        self.assertTrue('customer_phone' in form.fields)

    def test_order_form_required_fields(self):
        """Test whether the OrderForm validation fails for missing required
        fields."""
        form = OrderForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors['customer_name'],
            ['This field is required.']
            )
        self.assertEqual(
            form.errors['customer_email'],
            ['This field is required.']
            )
        self.assertEqual(
            form.errors['customer_address1'],
            ['This field is required.']
            )
        self.assertEqual(
            form.errors['customer_city'],
            ['This field is required.']
            )
        self.assertEqual(
            form.errors['customer_phone'],
            ['This field is required.']
            )
