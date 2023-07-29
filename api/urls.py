from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.views import ProductModelViewSet, BasketModelViewSet

app_name = 'api'

router = DefaultRouter()
router.register(r'products', ProductModelViewSet)
router.register(r'baskets', BasketModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
