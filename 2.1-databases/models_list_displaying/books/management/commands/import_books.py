import csv

from django.core.management.base import BaseCommand
from books.models import Book


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('books.csv', 'r', encoding='utf-8') as file:
            books = list(csv.DictReader(file, delimiter=';'))

        for book in books:
            Book.objects.create(**book)

        self.stdout.write(self.style.SUCCESS('Books imported'))
