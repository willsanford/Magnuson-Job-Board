# Generated by Django 3.0.2 on 2020-01-07 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='content',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='job',
            name='link',
            field=models.TextField(),
        ),
    ]
