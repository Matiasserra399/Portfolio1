# Generated by Django 4.2.7 on 2023-11-06 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='date',
        ),
        migrations.AddField(
            model_name='post',
            name='url',
            field=models.URLField(blank=True),
        ),
    ]
