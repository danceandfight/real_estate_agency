# Generated by Django 2.2.4 on 2020-04-01 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0003_flat_new_building'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flat',
            name='new_building',
            field=models.NullBooleanField(db_index=True, verbose_name='Новостройка'),
        ),
    ]
