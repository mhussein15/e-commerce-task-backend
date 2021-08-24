from django.db import models
from django.contrib.auth.models import User


class UserAddress(models.Model):
    user = models.OneToOneField(
        User, related_name='user_address', on_delete=models.CASCADE, null=True, blank=True)
    address = models.CharField(max_length=120)
    city = models.CharField(max_length=120)
    country = models.CharField(max_length=120)
    postal_code = models.CharField(max_length=120)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
