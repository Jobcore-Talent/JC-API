# Generated by Django 2.2.4 on 2019-11-11 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0047_remove_profile_profile_city_man'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='city',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]