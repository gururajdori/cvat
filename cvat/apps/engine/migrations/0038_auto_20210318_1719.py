# Generated by Django 3.1.7 on 2021-03-18 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0037_task_subset'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='access_key',
            field=models.CharField(default='', max_length=80),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='data',
            name='secreate_key',
            field=models.CharField(default='', max_length=80),
            preserve_default=False,
        ),
    ]
