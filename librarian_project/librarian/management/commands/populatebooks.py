from django.core.management.base import BaseCommand
from librarian.models import Author, Book
import random


def rand_isbn():
    part1 = str(random.randint(1000000, 9999999))
    part2 = str(random.randint(100000, 999999))
    return part1 + part2


BOOKS = [
    'vulture of dusk',
    'raven without hope',
    'witches of nightmares',
    'witches with vigor',
    'heirs and swindlers',
    'pilots and foes',
    'union of the night',
    'bane of stone',
    'searching for my home',
    'rejecting the sea',
    'opponent with wings',
    'girl without shame',
    'trees of desire',
    'swindlers of freedom',
    'defenders and mice',
    'cats and robots',
    'fruit without a home',
    'decay of the banished',
    'bathing in my dreams',
    'battling in the castle',
]


class Command(BaseCommand):

    def handle(self, *args, **options):
        for book in BOOKS:
            author = random.randint(28, 81)
            Book.objects.create(name=book,
                                author=Author.objects.get(pk=author),
                                isbn=rand_isbn())
        self.stdout.write(self.style.SUCCESS("Succesfully populated books"))

