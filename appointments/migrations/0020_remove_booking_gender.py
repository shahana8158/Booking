# Generated by Django 5.1.3 on 2025-01-28 10:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0019_booking_date_booking_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='Gender',
        ),
    ]
