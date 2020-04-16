# Generated by Django 2.2.4 on 2020-04-04 19:00

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('property', '0008_auto_20200403_1927'),
    ]

    operations = [
        migrations.AddField(
            model_name='flat',
            name='liked_by',
            field=models.ManyToManyField(blank=True, db_index=True, related_name='liked_posts', to=settings.AUTH_USER_MODEL),
        ),
    ]