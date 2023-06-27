from django.urls import reverse_lazy

from products.models import Product
from django.views.generic.edit import CreateView, UpdateView, DeleteView


class ProductFormView(CreateView):
    model = Product
    fields = ['name', 'description', 'price', 'quantity', 'category']


class ProductUpdateView(UpdateView):
    model = Product
    fields = ['price']
    template_name_suffix = "_update_form"


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy("web:create_product")
