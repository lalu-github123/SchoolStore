# Generated by Django 4.2.3 on 2023-07-27 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SSapp', '0002_purposes_studentform'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentform',
            name='address',
            field=models.CharField(max_length=250),
        ),
    ]
