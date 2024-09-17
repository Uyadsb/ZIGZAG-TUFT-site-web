from django.contrib import admin
from .models import Category, Item


# Register your models here.
admin.site.register(Category)


class ItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'price',  'category', 'is_sold',]
    list_editable = ['price', 'is_sold']
    list_display_links = ["name"]
    list_filter = ['category']

admin.site.register(Item, ItemAdmin)

admin.site.site_header= 'ZIGZAG TUFT'
admin.site.site_title = 'ZIGZAG TUFT'