# Generated by Django 3.0.8 on 2020-11-06 05:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20201028_2334'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='file',
            new_name='file_all',
        ),
    ]
