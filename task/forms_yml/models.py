from django.db import models
from .templates import worker


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

    def pars(self):
        self.vendor = worker.pars('task/items.yml', 'vendor')
        self.model = worker.pars('task/items.yml', 'model')
        self.price = worker.pars('task/items.yml', 'price')

    class Meta:
        verbose_name = 'Шина'
        verbose_name_plural = 'Шины'

    def __str__(self):
        return self.model