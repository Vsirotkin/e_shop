from django.conf import settings
from django.db import models


# my Models:

# item itself
class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()

    def __str__(self):
        return self.title


# inbetween stage: item when ordered (shopping card)
class OrderItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE,)

    def __str__(self):
        return self.item


# shopping card
class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
