# Generated by Django 4.2.16 on 2024-10-16 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_clickcounter_date_clickcounter_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clickcounter',
            name='date',
            field=models.DateField(default=None),
        ),
        migrations.AlterField(
            model_name='clickcounter',
            name='time',
            field=models.TimeField(default=None),
        ),
    ]
