# Generated by Django 3.2.9 on 2021-11-06 09:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0006_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='depth',
        ),
    ]
