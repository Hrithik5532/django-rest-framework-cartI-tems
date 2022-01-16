from django.contrib import admin

# Register your models here.
from .models import CartItem

@admin.register(CartItem)
class Cart_items(admin.ModelAdmin):
    list_display=['product_name','product_price','product_quantity']