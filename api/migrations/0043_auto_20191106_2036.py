# Generated by Django 2.2 on 2019-11-06 20:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0042_auto_20191104_1642'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentDeduction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('amount', models.FloatField()),
                ('employer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='deductions', to='api.Employer')),
            ],
        ),
    ]
