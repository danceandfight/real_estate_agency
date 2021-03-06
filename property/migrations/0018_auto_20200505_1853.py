# Generated by Django 2.2.4 on 2020-05-05 15:53

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('property', '0017_auto_20200419_1413'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Report_flat',
            new_name='FlatReport',
        ),
        migrations.AlterField(
            model_name='owner',
            name='flats_owned',
            field=models.ManyToManyField(blank=True, related_name='flats_owned_by', to='property.Flat', verbose_name='Квартиры в собственности'),
        ),
    ]
