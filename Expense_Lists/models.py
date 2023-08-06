from django.db import models
from django.contrib.auth.models import User


class Shop(models.Model):
    name = models.CharField('Shop', max_length=10)

    def __str__(self):
        return self.name.title()


class Product(models.Model):
    name = models.CharField('Type', max_length=10)

    def __str__(self):
        return self.name.title()


class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,
                             blank=True)
    # type = models.CharField(max_length=100)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True,
                                blank=True)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, null=True,
                             blank=True)
    cost = models.IntegerField()
    date = models.DateField()
    description = models.TextField(null=True, blank=True)
    paragon_image = models.ImageField(blank=True, null=True,
                                      upload_to="media/")

    def __str__(self):
        return self.shop.title()

    class Meta:
        ordering = ['date']
