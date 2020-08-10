# Generated by Django 2.2.8 on 2020-08-03 14:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0086_auto_20200802_1116'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payrates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hourly_rate', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('employer', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='employer_payrates_employer', to='api.Employer')),
                ('position', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='employer_payrates_positions', to='api.Position')),
            ],
        ),
        migrations.AddField(
            model_name='position',
            name='pay_rate',
            field=models.ManyToManyField(blank=True, related_name='pay_rate', through='api.Payrates', to='api.Employer'),
        ),
    ]
