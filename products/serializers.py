from rest_framework.relations import SlugRelatedField
from rest_framework.serializers import ModelSerializer

from products.models import Product, ProductCategory


class ProductSerializer(ModelSerializer):
    category = SlugRelatedField(slug_field='name', queryset=ProductCategory.objects.all())

    class Meta:
        model = Product
        fields = ('name', 'description', 'price', 'quantity', 'image', 'id', 'category')
