from django.contrib import admin
from django.contrib.admin import ModelAdmin, register
from showcase.models import Item, Order

admin.site.register(Order)

@register(Item)
class ItemAdmin(ModelAdmin):
    list_display = ('id', 'name', 'description', 'price')
