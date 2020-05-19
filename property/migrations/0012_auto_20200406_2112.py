# Generated by Django 2.2.4 on 2020-04-06 18:12
import phonenumbers
from django.db import migrations

def parse_phonenumbers(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.all():
        phonenumber = flat.owners_phonenumber
        normalized_phonenumber = phonenumbers.parse(phonenumber, "RU")
        if not phonenumbers.is_valid_number(normalized_phonenumber):
            continue
        flat.pure_phone_number = phonenumbers.format_number(
            normalized_phonenumber, 
            phonenumbers.PhoneNumberFormat.INTERNATIONAL
            )
        flat.save()

class Migration(migrations.Migration):

    dependencies = [
        ('property', '0011_flat_pure_phone_number'),
    ]

    operations = [
        migrations.RunPython(parse_phonenumbers)
    ]
