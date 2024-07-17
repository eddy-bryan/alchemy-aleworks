from django.test import SimpleTestCase

from .forms import BeerForm, MerchItemForm


class BeerFormTests(SimpleTestCase):
    """
    Test suite for the add beer form.

    These tests verify the behavior of the add beer form.
    """

    def test_beer_form_valid(self):
        """Test whether the add beer form is valid with valid data."""
        form_data = {
            'sku': 'test1234',
            'name': 'test',
            'type': 'test',
            'limited_edition': True,
            'description': 'test',
            'alcohol_content': 1.0,
            'price': 1.99
        }
        form = BeerForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_beer_form_invalid(self):
        """Test whether the add beer form is invalid with invalid data."""
        form_data = {
            'alcohol_content': 'A',
            'price': 'A'
        }
        form = BeerForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_beer_form_fields(self):
        """Test whether the BeerForm has the expected fields."""
        form = BeerForm()
        self.assertTrue('sku' in form.fields)
        self.assertTrue('name' in form.fields)
        self.assertTrue('type' in form.fields)
        self.assertTrue('limited_edition' in form.fields)
        self.assertTrue('description' in form.fields)
        self.assertTrue('alcohol_content' in form.fields)
        self.assertTrue('price' in form.fields)
        self.assertTrue('image_url' in form.fields)

    def test_beer_form_required_fields(self):
        """Test whether the BeerForm validation fails for missing required
        fields."""
        form = BeerForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors['name'],
            ['This field is required.']
            )
        self.assertEqual(
            form.errors['type'],
            ['This field is required.']
            )
        self.assertEqual(
            form.errors['description'],
            ['This field is required.']
            )
        self.assertEqual(
            form.errors['alcohol_content'],
            ['This field is required.']
            )
        self.assertEqual(
            form.errors['price'],
            ['This field is required.']
            )


class MerchItemFormTests(SimpleTestCase):
    """
    Test suite for the add merch form.

    These tests verify the behavior of the add merch form.
    """

    def test_merch_form_valid(self):
        """Test whether the add merch form is valid with valid data."""
        form_data = {
            'sku': 'test1234',
            'name': 'test',
            'category': 'test',
            'description': 'test',
            'sized_item': True,
            'price': 1.99
        }
        form = MerchItemForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_merch_form_invalid(self):
        """Test whether the add merch form is invalid with invalid data."""
        form_data = {
            'price': 'A'
        }
        form = MerchItemForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_merch_form_fields(self):
        """Test whether the MerchForm has the expected fields."""
        form = MerchItemForm()
        self.assertTrue('sku' in form.fields)
        self.assertTrue('name' in form.fields)
        self.assertTrue('category' in form.fields)
        self.assertTrue('description' in form.fields)
        self.assertTrue('sized_item' in form.fields)
        self.assertTrue('price' in form.fields)
        self.assertTrue('image_url' in form.fields)

    def test_merch_form_required_fields(self):
        """Test whether the MerchForm validation fails for missing required
        fields."""
        form = MerchItemForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors['name'],
            ['This field is required.']
            )
        self.assertEqual(
            form.errors['category'],
            ['This field is required.']
            )
        self.assertEqual(
            form.errors['description'],
            ['This field is required.']
            )
        self.assertEqual(
            form.errors['price'],
            ['This field is required.']
            )
