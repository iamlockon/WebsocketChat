# Generated by Django 2.0.6 on 2018-07-21 11:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chatapp', '0004_message'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='file',
        ),
        migrations.RemoveField(
            model_name='message',
            name='image',
        ),
    ]
