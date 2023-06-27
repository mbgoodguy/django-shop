from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from products.models import Product


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
