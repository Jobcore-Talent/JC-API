# Generated by Django 2.2.8 on 2021-11-24 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0116_employeepayment_over_time_earnings'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeepayment',
            name='hourly_rate',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10),
        ),
    ]
