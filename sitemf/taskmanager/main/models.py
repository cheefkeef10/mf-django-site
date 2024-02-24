from django.db import models
from tinymce.models import HTMLField

class News(models.Model):
    headline = models.CharField('Главный Заголовок', max_length=255)
    description = HTMLField('Описание')
    datetime = models.DateTimeField('Дата')

    def __str__(self):
        return self.headline


class Files(models.Model):
    text = models.CharField('Текст', max_length=100)
    specifications = models.FileField(upload_to='media', null=True)

    def __str__(self):
        return self.text


class nalogovaya(models.Model):
    ID = models.AutoField(primary_key=True)
    oktmo_id = models.CharField('ОКТМО', max_length=500)
    datetime = models.DateTimeField('ДатаЗач')
    INNADB = models.CharField('ИННАДБ', max_length=500)
    INNUL = models.CharField('ИННЮЛ', max_length=500)
    KBK = models.CharField('КБК', max_length=500)
    KPP = models.CharField('КПП', max_length=500)
    KPPADB = models.CharField('КППАДБ', max_length=500)
    NAIMPLAT = models.CharField('НАИМПЛАТ', max_length=500)
    SUM = models.CharField('СУМЗАЧ', max_length=500)


    def __str__(self):
        return self.oktmo_id





