from django.contrib import admin
from django.contrib.admin import ModelAdmin, register
from showcase.models import Item


@register(Item)
class ItemAdmin(ModelAdmin):
    list_display = ('id', 'name', 'description', 'price')
