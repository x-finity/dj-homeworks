import csv

from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone in phones:
            phone['slug'] = phone['name'].lower().replace(' ', '-')
            Phone.objects.create(**phone)

        self.stdout.write(self.style.SUCCESS('Phones imported'))
