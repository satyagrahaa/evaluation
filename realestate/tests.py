from django.test import TestCase

from .models import Property


class PropertyTestCase(TestCase):
    def test_property_str(self):
        new_property = Property(title="Apartment Rent")
        message = 'Apartment Rent'
        self.assertEqual(message, str(new_property))

    def test_str_property_title_is_not(self):
        new_property = Property()
        message = 'Untitled'
        self.assertEqual(message, str(new_property))
