# Generated by Django 2.2.4 on 2020-04-19 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0016_auto_20200415_2028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='flats_owned',
            field=models.ManyToManyField(blank=True, db_index=True, related_name='flats_owned_by', to='property.Flat', verbose_name='Квартиры в собственности'),
        ),
    ]