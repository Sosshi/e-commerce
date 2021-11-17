# Generated by Django 4.0b1 on 2021-11-15 19:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='added_by',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='products_added', to='users.customuser'),
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='products.category'),
        ),
        migrations.AddField(
            model_name='product',
            name='colors',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='products.color'),
        ),
        migrations.AddField(
            model_name='product',
            name='images',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='products.productimage'),
        ),
        migrations.AddField(
            model_name='product',
            name='shipping_price',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='products.shippingcost'),
        ),
        migrations.AddField(
            model_name='product',
            name='sizes',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='products.size'),
        ),
        migrations.AddField(
            model_name='product',
            name='suppliers',
            field=models.ManyToManyField(related_name='product', to='products.Supplier'),
        ),
        migrations.AddField(
            model_name='product',
            name='tags',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='products.tag'),
        ),
    ]