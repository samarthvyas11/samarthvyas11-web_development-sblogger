# Generated by Django 3.1.3 on 2021-01-11 19:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20210111_0052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='timeStamp',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
    ]
