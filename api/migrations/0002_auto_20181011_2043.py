# Generated by Django 2.0 on 2018-10-11 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='stop_receiving_invites',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='shiftemployee',
            name='comments',
            field=models.TextField(blank=True, max_length=450),
        ),
    ]
