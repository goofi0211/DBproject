# Generated by Django 3.0.3 on 2020-05-23 12:43

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('distributor', '0002_auto_20200523_2043'),
        ('shop', '0006_auto_20200522_1221'),
        ('boss', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='boss',
            name='gian',
        ),
        migrations.CreateModel(
            name='Supply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profit', models.PositiveIntegerField()),
                ('created_date', models.DateTimeField(default=datetime.datetime(2020, 5, 23, 12, 43, 52, 652959, tzinfo=utc))),
                ('boss', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='boss.Boss')),
                ('commodity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Commodity')),
                ('distributor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='distributor.Distributor')),
            ],
        ),
    ]