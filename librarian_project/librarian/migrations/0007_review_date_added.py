# Generated by Django 3.1.7 on 2021-03-29 10:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('librarian', '0006_auto_20210329_1037'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
