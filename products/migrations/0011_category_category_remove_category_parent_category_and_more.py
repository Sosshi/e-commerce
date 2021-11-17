# Generated by Django 4.0b1 on 2021-11-17 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_remove_product_images_product_images'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='category',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.RemoveField(
            model_name='category',
            name='parent_category',
        ),
        migrations.AddField(
            model_name='category',
            name='parent_category',
            field=models.ManyToManyField(blank=True, null=True, to='products.Category'),
        ),
    ]