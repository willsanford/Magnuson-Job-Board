# Generated by Django 3.0.2 on 2020-01-08 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0003_auto_20200107_1613'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='location',
            field=models.TextField(default=' '),
            preserve_default=False,
        ),
    ]
