from django.db import models
from products.models import Product
from django.contrib.auth.models import User

# Create your models here.


class Order(models.Model):
    user = models.ForeignKey(User, related_name='user', blank=True,
                             on_delete=models.CASCADE)
    total = models.IntegerField(blank=True,null=True)
    accepted = models.BooleanField(blank=True,null=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def get_total(self):
        total = 0
        for order_item in self.order_item.all():
            total += order_item.get_total_price()
        return total

    def __str__(self):
        return "%s %s" % (self.user, self.total)


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order, related_name='order_item', on_delete=models.CASCADE, blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    created_on = models.DateTimeField(auto_now_add=True)

    def get_total_price(self):
        return self.quantity * self.product.price

    def __str__(self):
        return self.product.name
