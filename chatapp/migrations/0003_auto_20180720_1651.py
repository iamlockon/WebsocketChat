# Generated by Django 2.0.6 on 2018-07-20 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatapp', '0002_room_topic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='max_capacity',
            field=models.IntegerField(default=2),
        ),
    ]
