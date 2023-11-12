import csv
from django.conf import settings
from django.core.management.base import BaseCommand
from EarthquakeApp.models import Earthquakes


class Command(BaseCommand):
    help = 'Load data from Earthquakes file'

    def handle(self, *args, **kwargs):
        data_file = settings.BASE_DIR / 'data' / 'earthquakes.csv'
        keys = ('Date', 'Time', 'Latitude', 'Longitude', 'Depth', 'Magnitude')  # the CSV columns we will gather data from.

        records = []
        with open(data_file, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                records.append({k: row[k] for k in keys})

        # extract the latitude and longitude from the Point object
        for record in records:
            # add the data to the database
            Earthquakes.objects.get_or_create(
                date=record['Date'],
                time=record['Time'],
                latitude=record['Latitude'],
                longitude=record['Longitude'],
                depth=record['Depth'],
                magnitude=record['Magnitude']
            )