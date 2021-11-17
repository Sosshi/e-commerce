# Generated by Django 4.0b1 on 2021-11-17 13:33

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('customer', '0003_alter_cart_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='user',
        ),
        migrations.AddField(
            model_name='cart',
            name='user',
            field=models.ManyToManyField(related_name='cart_items', to=settings.AUTH_USER_MODEL),
        ),
    ]
