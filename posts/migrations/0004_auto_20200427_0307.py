# Generated by Django 3.0.5 on 2020-04-26 22:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20200427_0240'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='slug_url',
            new_name='slug',
        ),
    ]
