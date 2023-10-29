from django.test import TestCase
from .models import Location

class LocationModelTest(TestCase):
    def test_create_location(self):
        # Create a Location object
        location = Location.objects.create(
            name='Karachi',
            max_daily_visitors=100,
            users_per_day=0
        )

        # Retrieve the Location object from the database
        retrieved_location = Location.objects.get(name='Karachi')

        self.assertEqual(location, retrieved_location)

    def test_location_str_method(self):
        # Create a Location object
        location = Location.objects.create(
            name='Lahore',
            max_daily_visitors=200,
            users_per_day=0
        )

        self.assertEqual(str(location), 'Lahore')


