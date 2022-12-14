# Generated by Django 2.2.8 on 2021-11-24 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0115_payrollperiod_total_employees'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeepayment',
            name='over_time_earnings',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='overtime earnings'),
        ),
    ]
