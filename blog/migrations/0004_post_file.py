# Generated by Django 3.0.8 on 2020-10-29 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200917_0101'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='file',
            field=models.FileField(default='default.jpg', upload_to='uploads'),
        ),
    ]
