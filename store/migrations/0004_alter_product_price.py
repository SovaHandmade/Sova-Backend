# Generated by Django 5.1.1 on 2024-10-12 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0003_alter_product_form_alter_product_topic"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="price",
            field=models.IntegerField(default=0),
        ),
    ]
