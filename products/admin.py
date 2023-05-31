from django.contrib import admin
from products.models import Product, ProductCategory
from users.models import User

# Register your models here.
admin.site.register(Product)
admin.site.register(ProductCategory)
admin.site.register(User)
