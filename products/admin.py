from django.contrib import admin

from products.models import Product, ProductCategory

# Register your models here.
admin.site.register(ProductCategory)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'category', 'id', 'stripe_product_price_id')
    fields = ('name', 'description', 'stripe_product_price_id', ('price', 'quantity'), 'image', 'category', 'id', )
    readonly_fields = ('id',)
    search_fields = ('name',)
    ordering = ('name', 'id')
