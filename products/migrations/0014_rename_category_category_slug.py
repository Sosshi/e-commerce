# Generated by Django 4.0b1 on 2021-11-17 21:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_alter_category_parent_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='category',
            new_name='slug',
        ),
    ]
