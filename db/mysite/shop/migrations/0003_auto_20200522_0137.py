# Generated by Django 3.0.3 on 2020-05-21 17:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20200521_1739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commodity',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True),
        ),
    ]
