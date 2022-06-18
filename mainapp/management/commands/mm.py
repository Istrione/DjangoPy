from django.core.management import BaseCommand
from django.core.management import call_command


class Command(BaseCommand):
    def handle(self, *args, **options):
        call_command('makemessages', '--locale=ru', '--ignore=venv', '--no-location')