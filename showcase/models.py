from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Item(models.Model):
    name = models.CharField(max_length=100, verbose_name='название товара')
    description = models.TextField(verbose_name='описание товара')
    price = models.PositiveIntegerField(verbose_name='цена товара')

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'


class Order(models.Model):
    items = models.ManyToManyField(Item)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='recipe',
        blank=True,
        null=True
    )
