# Generated by Django 3.2.12 on 2022-03-17 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0121_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='stripe_sub_id',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
