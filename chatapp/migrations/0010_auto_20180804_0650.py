# Generated by Django 2.0.6 on 2018-08-04 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatapp', '0009_auto_20180804_0324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='users',
            field=models.CharField(default=set(), max_length=200),
        ),
    ]
