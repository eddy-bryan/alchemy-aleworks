from django.test import SimpleTestCase
from django.urls import reverse


class StaticViewTests(SimpleTestCase):
    """
    Test suite for static views within the project.

    These tests focus on views that render static content or perform basic
    actions.
    """
    def test_taproom_view_reverse(self):
        """Test whether the taproom page URL resolves correctly."""
        response = self.client.get(reverse("taproom"))
        self.assertEqual(response.status_code, 200)

    def test_taproom_page_template(self):
        """Test whether the taproom page uses the correct template."""
        response = self.client.get(reverse("taproom"))
        self.assertTemplateUsed(response, "pages/taproom.html")

    def test_taproom_page_content(self):
        """Test whether the taproom page contains expected content."""
        response = self.client.get(reverse("taproom"))
        self.assertContains(response, "Visit Our Taproom")
        self.assertNotContains(response, "Not on the page")

    def test_orders_and_returns_view_reverse(self):
        """
        Test whether the orders and returns page URL resolves correctly.
        """
        response = self.client.get(reverse("orders_and_returns"))
        self.assertEqual(response.status_code, 200)

    def test_orders_and_returns_page_template(self):
        """
        Test whether the orders and returns page uses the correct template.
        """
        response = self.client.get(reverse("orders_and_returns"))
        self.assertTemplateUsed(response, "pages/orders_and_returns.html")

    def test_orders_and_returns_page_content(self):
        """
        Test whether the orders and returns page contains expected content.
        """
        response = self.client.get(reverse("orders_and_returns"))
        self.assertContains(response, "Last Updated")
        self.assertNotContains(response, "Not on the page")

    def test_privacy_policy_view_reverse(self):
        """
        Test whether the orders and returns page URL resolves correctly.
        """
        response = self.client.get(reverse("privacy_policy"))
        self.assertEqual(response.status_code, 200)

    def test_privacy_policy_page_template(self):
        """
        Test whether the orders and returns page uses the correct template.
        """
        response = self.client.get(reverse("privacy_policy"))
        self.assertTemplateUsed(response, "pages/privacy_policy.html")

    def test_privacy_policy_page_content(self):
        """
        Test whether the orders and returns page contains expected content.
        """
        response = self.client.get(reverse("privacy_policy"))
        self.assertContains(response, "Effective")
        self.assertNotContains(response, "Not on the page")

    def test_terms_and_conditions_view_reverse(self):
        """
        Test whether the terms and conditions page URL resolves correctly.
        """
        response = self.client.get(reverse("terms_and_conditions"))
        self.assertEqual(response.status_code, 200)

    def test_terms_and_conditions_page_template(self):
        """
        Test whether the terms and conditions page uses the correct template.
        """
        response = self.client.get(reverse("terms_and_conditions"))
        self.assertTemplateUsed(response, "pages/terms_and_conditions.html")

    def test_terms_and_conditions_page_content(self):
        """
        Test whether the terms and conditions page contains expected content.
        """
        response = self.client.get(reverse("terms_and_conditions"))
        self.assertContains(response, "Last Updated")
        self.assertNotContains(response, "Not on the page")
