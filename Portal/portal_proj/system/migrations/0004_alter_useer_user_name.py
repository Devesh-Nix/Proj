# Generated by Django 5.1.6 on 2025-02-09 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0003_rename_user_useer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useer',
            name='user_name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
