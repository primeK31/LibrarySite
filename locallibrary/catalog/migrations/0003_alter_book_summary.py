# Generated by Django 4.2.4 on 2023-08-19 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_language_book_language'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='summary',
            field=models.TextField(blank=True, help_text='Enter a brief description of the book', max_length=1000),
        ),
    ]
