# Generated by Django 4.2.9 on 2024-02-13 14:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_rename_oktmo_id_nalogovaya_oktmo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='nalogovaya',
            old_name='OKTMO',
            new_name='oktmo_id',
        ),
    ]
