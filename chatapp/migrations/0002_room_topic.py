# Generated by Django 2.0.6 on 2018-07-20 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='topic',
            field=models.CharField(default='Programming', max_length=30),
        ),
    ]
