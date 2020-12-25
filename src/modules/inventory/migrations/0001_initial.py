# Generated by Django 3.1.4 on 2020-12-24 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(default=None, max_length=255, verbose_name='description')),
                ('unit_price', models.IntegerField(default=0, verbose_name='unit price')),
                ('stock', models.IntegerField(default=0, verbose_name='stock')),
            ],
        ),
    ]
