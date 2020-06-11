from django.db import models
from django.utils import timezone
from shop.models import Commodity
from customer.models import Customer
from django.urls import reverse
# Create your models here.
class Distributor(models.Model):
    name=models.CharField(max_length=200,blank=False)
    margin=models.PositiveIntegerField()
    tell=models.CharField(max_length=200,blank=False)
    mail=models.EmailField(blank=True)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('distributor_detail',args=(self.id, self.name,))

class Sales(models.Model):
    seller=models.ForeignKey('Distributor', on_delete=models.CASCADE)
    commodity=models.ForeignKey('shop.Commodity', on_delete=models.CASCADE)
    customer=models.ForeignKey('customer.Customer', on_delete=models.CASCADE)
    profit=models.PositiveIntegerField()
    created_date = models.DateTimeField(
        default=timezone.now()
    )
    def __str__(self):
        return self.seller.name
