from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Author(models.Model):
    author = models.CharField(max_length=64, blank=True)

    def __str__(self):
        return f'{self.author}'


class Book(models.Model):
    name = models.CharField(max_length=128, blank=True, unique=True)
    isbn = models.CharField(max_length=32, blank=True, unique=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fav_books = models.ManyToManyField(Book)
    fav_authors = models.ManyToManyField(Author)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    def __str__(self):
        return f'{self.user}'


class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    points = models.IntegerField(default=0)
    date_added = models.DateTimeField(auto_now_add=True)
    #TODO: dodawanie recenzji i ocennianie ich i komentarze
    # nowy model review comments?