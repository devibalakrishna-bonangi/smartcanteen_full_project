from django.db import models

class MenuItem(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    desc = models.TextField()
    image = models.TextField()  # store image URL
    category = models.CharField(max_length=100)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    items = models.JSONField()
    total = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)
