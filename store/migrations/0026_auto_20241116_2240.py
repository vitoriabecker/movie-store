# Generated by Django 3.2.25 on 2024-11-17 01:40

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0025_auto_20241113_2204'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='active',
        ),
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 11, 17, 1, 40, 24, 788336, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='movie',
            name='poster',
            field=models.ImageField(null=True, upload_to='media/posters'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='published_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 11, 17, 1, 40, 24, 787797, tzinfo=utc)),
        ),
    ]