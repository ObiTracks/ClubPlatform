# Generated by Django 3.2.6 on 2021-09-18 02:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainplatform', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='date',
        ),
    ]
