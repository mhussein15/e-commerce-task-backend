from django.db import models
from django.utils.text import slugify

# Create your models here.


def upload_to(instance, filename):
    return 'products/{filename}'.format(filename=filename)


class Category(models.Model):
    name = models.CharField(max_length=120, unique=True)
    desc = models.TextField()
    image = models.ImageField(upload_to=upload_to, null=True)
    slug = models.SlugField(max_length=100, blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
