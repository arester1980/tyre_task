from django.db import models


class Vendor(models.Model):
    vendor = models.CharField(max_length=250, verbose_name='Производитель')

    def __str__(self):
        return self.vendor

    class Meta:
        verbose_name = 'Производитель'
        verbose_name_plural = 'Производители'


class Tyre(models.Model):
    vendor = models.ManyToManyField(Vendor)
    model = models.CharField(max_length=250, verbose_name='Модель')
    price = models.IntegerField(default=0, verbose_name='Цена')

    def __str__(self):
        return self.model

    class Meta:
        verbose_name = 'Шина'
        verbose_name_plural = 'Шины'