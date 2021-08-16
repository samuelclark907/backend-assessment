# Generated by Django 3.2.6 on 2021-08-14 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=50)),
                ('authorId', models.CharField(max_length=50)),
                ('likes', models.CharField(max_length=50)),
                ('popularity', models.CharField(max_length=50)),
                ('reads', models.CharField(max_length=50)),
                ('tags', models.CharField(max_length=200)),
            ],
        ),
    ]