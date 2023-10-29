import os
import logging
from django.core.management.base import BaseCommand
from django.utils import timezone
from ads.models import Location

class Command(BaseCommand):
    help = 'Update users_per_day field for all locations'
    print("start")

    def handle(self, *args, **options):
        """This function sets the users_per_day value to 0 when date will change"""
        self.stdout.write('Starting the update process.')
        script_directory = os.path.dirname(os.path.abspath(__file__))
        log_file_path = os.path.join(script_directory, 'logs/update_users_per_day.log')

        # Configure the logger
        logging.basicConfig(filename=log_file_path, level=logging.INFO, format='%(asctime)s - %(message)s')

        logging.info('Starting the update process.')

        # Get all locations
        locations = Location.objects.all()

        # Update users_per_day to 0 for each location
        for location in locations:
            location.users_per_day = 0
            location.save()
            logging.info(f'users_per_day set to 0 for location: {location.name}')

        logging.info('Update process completed.')

        self.stdout.write(self.style.SUCCESS('Updated users_per_day for all locations.'))
