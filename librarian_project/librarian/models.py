from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=32, blank=True)
    last_name = models.CharField(max_length=32, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Book(models.Model):
    name = models.CharField(max_length=128, blank=True)
    isbn = models.CharField(max_length=32, blank=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'


