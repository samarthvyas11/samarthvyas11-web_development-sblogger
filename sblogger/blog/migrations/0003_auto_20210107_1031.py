# Generated by Django 3.1.3 on 2021-01-07 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210105_0021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(default='', max_length=100),
        ),
    ]
