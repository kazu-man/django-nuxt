# Generated by Django 2.2.13 on 2021-10-26 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_item_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='memo',
            field=models.TextField(blank=True, verbose_name='メモ'),
        ),
    ]
