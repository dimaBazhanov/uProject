# Generated by Django 2.1.5 on 2020-10-27 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0004_flat_flatdetails'),
    ]

    operations = [
        migrations.AddField(
            model_name='flatdetails',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
