# Generated by Django 4.2.9 on 2024-02-08 07:20

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='headline2',
        ),
        migrations.AlterField(
            model_name='news',
            name='description',
            field=tinymce.models.HTMLField(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='news',
            name='headline',
            field=models.CharField(max_length=255, verbose_name='Главный Заголовок'),
        ),
    ]
