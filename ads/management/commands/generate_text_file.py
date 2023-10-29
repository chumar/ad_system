import os
import datetime
from django.core.management.base import BaseCommand
from django.conf import settings
from ads.models import Ad, FileStored, UserVisit
from django.db.models import Sum
import logging

class Command(BaseCommand):
    help = 'Generate and store a text file with ad information daily after 12 PM'

    def handle(self, *args, **options):
        """This command generates text files with ad information for each ad and stores them.
        Each file contains details about ad visits and user statistics."""

        # Configure the logger for this script
        script_directory = os.path.dirname(os.path.abspath(__file__))
        log_file_path = os.path.join(script_directory, 'logs/generate_text_file.log')
        logging.basicConfig(filename=log_file_path, level=logging.INFO, format='%(asctime)s - %(message)s')

        now = datetime.datetime.now()

        logger = logging.getLogger(__name__)

        for ad in Ad.objects.all():
            content = self.generate_text_content(ad)
            file_name = f"file_{now.date()}_{ad.ad_name}.txt"
            file_relative_path = os.path.join('files', file_name)

            with open(os.path.join(settings.MEDIA_ROOT, file_relative_path), 'w') as file:
                file.write(content)

            # Create a new FileStored object and save it with the relative path
            file_stored = FileStored(date=now.date(), content=content, file=file_relative_path)
            file_stored.save()

            self.stdout.write(self.style.SUCCESS(f'File for ad "{ad.ad_name}" stored successfully.'))

            # Send a simple message to the log file
            logger.info(f'File for ad "{ad.ad_name}" stored successfully.')


    def generate_text_content(self, ad):
        """Generate text content for an ad."""
        all_ads_data = []

        for location in ad.locations.all():
            total_allowed_users = location.max_daily_visitors
            users_per_day_for_location = location.users_per_day
            ad_name = ad.ad_name  # Get the current ad_name

            ad_data = (
                f"Ad-name: {ad_name}\nLocation: {location.name}\n"
                f"Total no of users allowed for {ad_name} per day: {total_allowed_users}\n"
                f"Total users from {location.name} viewed {ad_name} per day: {users_per_day_for_location}"
            )

            user_visits = UserVisit.objects.filter(ad=ad, user__createuser__location=location).values(
                'user__username').annotate(total_visits=Sum('view_count'))

            user_data = []
            for user_visit in user_visits:
                user_name = user_visit['user__username']
                total_visits = user_visit['total_visits']
                user_data.append(f"{user_name} viewed the {ad_name} for {total_visits} times")

            all_ads_data.append(ad_data)
            all_ads_data.append("Viewed Details of each User")
            all_ads_data.extend(user_data)
            all_ads_data.append("----------------------------------")

        return "\n".join(all_ads_data)
