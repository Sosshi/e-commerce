# Generated by Django 4.0b1 on 2021-11-15 20:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_category_thumbnail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='thumbnail',
        ),
    ]
