from decimal import MIN_EMIN
from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=100, verbose_name = 'название товара')
    description = models.TextField(verbose_name = 'описание товара')
    price = models.PositiveIntegerField(verbose_name='цена товара')
    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'