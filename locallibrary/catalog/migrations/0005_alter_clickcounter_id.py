# Generated by Django 4.2.16 on 2024-10-16 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_alter_clickcounter_date_alter_clickcounter_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clickcounter',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
