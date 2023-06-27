from django.contrib import admin
from products.models import Product, ProductCategory

# Register your models here.
admin.site.register(ProductCategory)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'category', 'id')
    fields = ('name', 'description', ('price', 'quantity'), 'image', 'category', 'id')
    readonly_fields = ('id',)
    search_fields = ('name',)
    ordering = ('name', 'id')

