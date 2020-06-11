# Generated by Django 3.0.3 on 2020-05-23 12:50

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('distributor', '0002_auto_20200523_2043'),
    ]

    operations = [
        migrations.AddField(
            model_name='distributor',
            name='mail',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AddField(
            model_name='distributor',
            name='tell',
            field=models.CharField(default=123, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='sales',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 23, 12, 50, 14, 932720, tzinfo=utc)),
        ),
    ]