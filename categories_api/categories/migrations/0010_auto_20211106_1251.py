# Generated by Django 3.2.9 on 2021-11-06 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0009_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='similar_category_id',
        ),
        migrations.AddField(
            model_name='category',
            name='similar_category',
            field=models.ManyToManyField(blank=True, related_name='_categories_category_similar_category_+', to='categories.Category'),
        ),
    ]