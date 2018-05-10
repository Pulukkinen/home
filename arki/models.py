from django.db import models
from django.contrib.auth.models import User

class Expence(models.Model):
    exp_title = models.CharField(max_length=128)
    amount = models.DecimalField(max_digits=19, decimal_places=2)
    receipt = models.ImageField(upload_to='img',null=True, blank=True)
    payer = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.exp_title

class Item(models.Model):
    name = models.CharField(max_length=128)
    def __str__(self):
        return self.name

class Shoplist(models.Model):
    title = models.CharField(max_length=128)
    items = models.ManyToManyField(Item, blank=True)
    def __str__(self):
        return self.title