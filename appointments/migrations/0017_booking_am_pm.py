# Generated by Django 5.1.3 on 2025-01-26 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0016_remove_booking_time_period'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='AM_PM',
            field=models.CharField(blank=True, choices=[('AM', 'AM'), ('PM', 'PM')], max_length=2, null=True),
        ),
    ]
