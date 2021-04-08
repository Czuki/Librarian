# Generated by Django 3.1.7 on 2021-03-28 18:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('librarian', '0004_auto_20210327_1218'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('points', models.IntegerField(default=0)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='librarian.book')),
                ('reviewer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='librarian.profile')),
            ],
        ),
        migrations.CreateModel(
            name='AuthorReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('points', models.IntegerField(default=0)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='librarian.author')),
                ('reviewer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='librarian.profile')),
            ],
        ),
    ]