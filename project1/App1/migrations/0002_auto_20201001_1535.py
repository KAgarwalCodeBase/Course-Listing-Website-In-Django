# Generated by Django 3.1.1 on 2020-10-01 15:35

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='details',
            old_name='il',
            new_name='ct',
        ),
        migrations.RemoveField(
            model_name='details',
            name='sp',
        ),
        migrations.AddField(
            model_name='allcourses',
            name='startedfrom',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 1, 15, 35, 49, 504565, tzinfo=utc), verbose_name='Started From'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='details',
            name='your_choice',
            field=models.BooleanField(default=False),
        ),
    ]
