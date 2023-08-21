from django.db import models

from products.models import Basket
from users.models import User


# Create your models here.
class Order(models.Model):
    STATUSES = [
        ('1', 'Создан'),
        ('2', 'Оплачен'),
        ('3', 'В пути'),
        ('4', 'Доставлен'),
    ]

    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.CharField(max_length=256)
    address = models.CharField(max_length=256)
    basket_history = models.JSONField(default=dict)
    created = models.DateTimeField(auto_now_add=True)
    initiator = models.ForeignKey(to=User, on_delete=models.CASCADE)
    status = models.CharField(max_length=6, choices=STATUSES, default='1')

    def __str__(self):
        return f'Order №{self.id}. {self.first_name} {self.last_name}'

    def update_after_payment(self):
        baskets = Basket.objects.filter(user=self.initiator)
        self.status = '2'
        self.basket_history = {
            'purchased_items': [basket.de_json() for basket in baskets],
            'total_sum': float(baskets.total_sum()),
        }

        baskets.delete()
        self.save()
