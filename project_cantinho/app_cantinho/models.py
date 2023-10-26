from django.db import models
from django.contrib.auth.models import User
class Product(models.Model):
  name = models.CharField(max_length=200)
  value = models.DecimalField(max_digits=10, decimal_places=2)
  link = models.URLField()
  stock = models.IntegerField(default=0)
  disponivel = models.BooleanField(default=True)
  def __str__(self):
    return self.name

class Vendinha(models.Model):
  name = models.CharField(max_length=200)
  products = models.ManyToManyField(Product)


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null = True, blank = True)
    products = models.ManyToManyField(Product, blank = True)
    total = models.DecimalField(default = 0.00, max_digits=100, decimal_places = 2)
    
    def __str__(self):
        return str(self.id)
class VendinhaController():
  def get_vendinha_by_name(name):
    return Vendinha.objects.get(name=name)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
    