# Generated by Django 2.0 on 2018-09-28 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0031_auto_20180928_2214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='availabilityblock',
            name='ending_at',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='availabilityblock',
            name='starting_at',
            field=models.DateTimeField(blank=True),
        ),
    ]