# Generated by Django 4.2.9 on 2024-02-13 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_delete_barguzinsky_delete_bauntovsky_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='nalogovaya',
            name='oktmo_id',
            field=models.IntegerField(default=0, verbose_name='октмоайди'),
            preserve_default=False,
        ),
    ]