# Generated by Django 2.0.6 on 2018-08-04 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatapp', '0008_auto_20180803_1543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='users',
            field=models.CharField(default=[], max_length=200),
        ),
    ]
