from django.db import models
from django.db.models.fields import SlugField
from category.models import Category
from django.utils.text import slugify
# Create your models here.


def upload_to(instance, filename):
    return 'products/{filename}'.format(filename=filename)


class Product(models.Model):
    name = models.CharField(max_length=120)
    desc = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(upload_to=upload_to, null=True)
    category = models.ManyToManyField(Category, related_name='products')
    slug = models.SlugField(max_length=100, blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
