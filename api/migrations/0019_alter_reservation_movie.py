# Generated by Django 5.1.3 on 2024-12-16 06:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0018_alter_reservation_person'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='movie',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='reservedMovie', to='api.movie'),
        ),
    ]