# Generated by Django 5.0.6 on 2024-07-09 17:01

import django_jsonform.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("example", "0002_alter_product_properties"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="properties",
            field=django_jsonform.models.fields.JSONField(),
        ),
    ]
