# Generated by Django 3.0.2 on 2020-01-16 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='role_type',
        ),
        migrations.AlterField(
            model_name='job',
            name='date_due',
            field=models.DateField(),
        ),
    ]
