# Generated by Django 3.0.5 on 2020-04-26 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug_url',
            field=models.SlugField(blank=True),
        ),
    ]
