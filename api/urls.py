from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import BasketModelViewSet, ProductModelViewSet

app_name = 'api'

router = DefaultRouter()
router.register(r'products', ProductModelViewSet)
router.register(r'baskets', BasketModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
