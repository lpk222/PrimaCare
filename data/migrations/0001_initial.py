# Generated by Django 3.1.7 on 2021-03-06 11:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authentication', '0005_auto_20210306_1040'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('patient', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='authentication.patient')),
                ('name', models.CharField(max_length=200)),
                ('quantity', models.IntegerField()),
                ('timePeriod', models.CharField(choices=[('week', 'week'), ('day', 'day'), ('fortnight', 'fortnight')], max_length=200)),
            ],
        ),
    ]
