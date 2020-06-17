from django.db import models
import yaml
from django.core.files import File


class Vendor(models.Model):
    vendor = models.CharField(max_length=200, verbose_name='Производитель')

    class Meta:
        verbose_name = 'Производитель'
        verbose_name_plural = 'Производители'

    def __str__(self):
        return self.vendor


class Tyre(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    model = models.CharField(max_length=200, verbose_name='Модель')
    price = models.IntegerField(default=0, verbose_name='Цена $')

    class Meta:
        verbose_name = 'Шина'
        verbose_name_plural = 'Шины'

    def __str__(self):
        return self.model

class Incoming(models.Model):
    title = models.CharField(max_length=200, verbose_name='Имя файла')
    file = models.FileField(upload_to='media/')

    class Meta:
        verbose_name = 'Файл'
        verbose_name_plural = 'Файлы'

    def __str__(self):
        return self.title

