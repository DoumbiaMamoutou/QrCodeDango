# Generated by Django 2.2.5 on 2020-01-04 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nanapp', '0004_auto_20200103_1840'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='specialite',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
