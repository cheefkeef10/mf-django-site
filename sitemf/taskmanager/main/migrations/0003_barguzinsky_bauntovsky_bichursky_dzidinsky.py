# Generated by Django 4.2.9 on 2024-02-12 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_news_headline2_alter_news_description_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='barguzinsky',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('OKTMO', models.IntegerField(verbose_name='ОКТМО')),
                ('datetime', models.DateTimeField(verbose_name='ДатаЗач')),
                ('INNADB', models.CharField(max_length=500, verbose_name='ИННАДБ')),
                ('INNUL', models.CharField(max_length=500, verbose_name='ИННЮЛ')),
                ('KBK', models.CharField(max_length=500, verbose_name='КБК')),
                ('KPP', models.CharField(max_length=500, verbose_name='КПП')),
                ('KPPADB', models.CharField(max_length=500, verbose_name='КППАДБ')),
                ('NAIMPLAT', models.CharField(max_length=500, verbose_name='НАИМПЛАТ')),
                ('SUM', models.CharField(max_length=500, verbose_name='СУМЗАЧ')),
            ],
        ),
        migrations.CreateModel(
            name='bauntovsky',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('OKTMO', models.IntegerField(verbose_name='ОКТМО')),
                ('datetime', models.DateTimeField(verbose_name='ДатаЗач')),
                ('INNADB', models.CharField(max_length=500, verbose_name='ИННАДБ')),
                ('INNUL', models.CharField(max_length=500, verbose_name='ИННЮЛ')),
                ('KBK', models.CharField(max_length=500, verbose_name='КБК')),
                ('KPP', models.CharField(max_length=500, verbose_name='КПП')),
                ('KPPADB', models.CharField(max_length=500, verbose_name='КППАДБ')),
                ('NAIMPLAT', models.CharField(max_length=500, verbose_name='НАИМПЛАТ')),
                ('SUM', models.CharField(max_length=500, verbose_name='СУМЗАЧ')),
            ],
        ),
        migrations.CreateModel(
            name='Bichursky',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('OKTMO', models.IntegerField(verbose_name='ОКТМО')),
                ('datetime', models.DateTimeField(verbose_name='ДатаЗач')),
                ('INNADB', models.CharField(max_length=500, verbose_name='ИННАДБ')),
                ('INNUL', models.CharField(max_length=500, verbose_name='ИННЮЛ')),
                ('KBK', models.CharField(max_length=500, verbose_name='КБК')),
                ('KPP', models.CharField(max_length=500, verbose_name='КПП')),
                ('KPPADB', models.CharField(max_length=500, verbose_name='КППАДБ')),
                ('NAIMPLAT', models.CharField(max_length=500, verbose_name='НАИМПЛАТ')),
                ('SUM', models.CharField(max_length=500, verbose_name='СУМЗАЧ')),
            ],
        ),
        migrations.CreateModel(
            name='Dzidinsky',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('OKTMO', models.IntegerField(verbose_name='ОКТМО')),
                ('datetime', models.DateTimeField(verbose_name='ДатаЗач')),
                ('INNADB', models.CharField(max_length=500, verbose_name='ИННАДБ')),
                ('INNUL', models.CharField(max_length=500, verbose_name='ИННЮЛ')),
                ('KBK', models.CharField(max_length=500, verbose_name='КБК')),
                ('KPP', models.CharField(max_length=500, verbose_name='КПП')),
                ('KPPADB', models.CharField(max_length=500, verbose_name='КППАДБ')),
                ('NAIMPLAT', models.CharField(max_length=500, verbose_name='НАИМПЛАТ')),
                ('SUM', models.CharField(max_length=500, verbose_name='СУМЗАЧ')),
            ],
        ),
    ]