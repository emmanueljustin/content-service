# Generated by Django 5.1.3 on 2024-12-13 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_reservation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
    ]
