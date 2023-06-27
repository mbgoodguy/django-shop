from django.urls import path

from .views import ProductDeleteView, ProductFormView, ProductUpdateView

app_name = 'web'

urlpatterns = [
    path('product/', ProductFormView.as_view(), name='create_product'),
    path('product/<pk>', ProductUpdateView.as_view(), name='update_product'),
    path('product/<pk>/delete', ProductDeleteView.as_view(), name='delete_product'),
]
