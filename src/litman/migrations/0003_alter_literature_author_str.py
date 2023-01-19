# Generated by Django 4.1.5 on 2023-01-11 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('litman', '0002_rename_number_literature_issue'),
    ]

    operations = [
        migrations.AlterField(
            model_name='literature',
            name='author_str',
            field=models.TextField(blank=True, help_text='List of authors in the format "LastName, GivenName" separated by semi-colons. E.g Smith, John; Klose, Sarah;', null=True, verbose_name='authors'),
        ),
    ]
