# Generated by Django 2.0 on 2018-11-09 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20181109_1713'),
    ]

    operations = [
        migrations.AddField(
            model_name='employer',
            name='automatically_accept_from_favlists',
            field=models.BooleanField(default=True),
        ),
    ]