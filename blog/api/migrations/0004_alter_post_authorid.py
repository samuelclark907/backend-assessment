# Generated by Django 3.2.6 on 2021-08-16 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20210816_0052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='authorId',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
