# Generated by Django 5.1.4 on 2024-12-29 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cart", "0002_alter_order_total_cost"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="items",
            field=models.ManyToManyField(related_name="orders", to="cart.cartitem"),
        ),
    ]
