# Generated by Django 5.1.3 on 2024-12-03 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_wishlist'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExpensePriority',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expenseNamne', models.CharField(max_length=255)),
                ('budget', models.DecimalField(decimal_places=2, max_digits=7)),
                ('acquired', models.BooleanField()),
                ('priority', models.IntegerField()),
                ('note', models.CharField(max_length=255)),
            ],
        ),
    ]
