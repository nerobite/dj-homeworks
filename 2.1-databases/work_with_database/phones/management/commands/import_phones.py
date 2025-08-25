import csv
from datetime import datetime
from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    help = 'Imports phones from a CSV file'
    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='The path to the CSV file')

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone in phones:
            # Преобразование даты выпуска в объект datetime
            release_date = datetime.strptime(phone['release_date'], '%Y-%m-%d').date()
            # Преобразование булевого значения
            lte_exists = phone['lte_exists'].lower() == 'true'
            # Создание и сохранение объекта модели
            Phone.objects.create(
                name=phone['name'],
                price=phone['price'],
                image=phone['image'],
                release_date=release_date,
                lte_exists=lte_exists,
            )
            self.stdout.write(self.style.SUCCESS(f'Successfully imported phone: {phone["name"]}'))