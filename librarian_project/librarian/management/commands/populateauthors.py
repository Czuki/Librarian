from django.core.management.base import BaseCommand
from librarian.models import Author

from faker import Factory


def create_name():
    fake = Factory.create("pl_PL")
    first_name = fake.first_name()
    last_name = fake.last_name()
    return first_name, last_name


def create_author():
    for author in range(50):
        first_name, last_name = create_name()
        Author.objects.create(first_name=first_name,
                              last_name=last_name)


class Command(BaseCommand):

    def handle(self, *args, **options):
        create_author()
        self.stdout.write(self.style.SUCCESS("Succesfully populated authors"))
