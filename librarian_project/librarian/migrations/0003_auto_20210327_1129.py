# Generated by Django 3.1.7 on 2021-03-27 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('librarian', '0002_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='fav_authors',
        ),
        migrations.AddField(
            model_name='profile',
            name='fav_authors',
            field=models.ManyToManyField(to='librarian.Author'),
        ),
        migrations.RemoveField(
            model_name='profile',
            name='fav_books',
        ),
        migrations.AddField(
            model_name='profile',
            name='fav_books',
            field=models.ManyToManyField(to='librarian.Book'),
        ),
    ]