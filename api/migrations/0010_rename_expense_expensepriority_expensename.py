# Generated by Django 5.1.3 on 2024-12-04 08:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_rename_expensename_expensepriority_expense'),
    ]

    operations = [
        migrations.RenameField(
            model_name='expensepriority',
            old_name='expense',
            new_name='expenseName',
        ),
    ]
