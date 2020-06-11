from django.db import models
from django.utils import timezone
# Create your models here.
class Boss(models.Model):
    name=models.CharField(max_length=200,blank=False)
    tell=models.CharField(max_length=200,blank=False)
    mail=models.EmailField()
    def __str__(self):
        return self.name

class Supply(models.Model):
    boss=models.ForeignKey('Boss', on_delete=models.CASCADE)
    commodity=models.ForeignKey('shop.Commodity', on_delete=models.CASCADE)
    distributor=models.ForeignKey('distributor.Distributor', on_delete=models.CASCADE)
    profit=models.PositiveIntegerField()
    created_date = models.DateTimeField(
        default=timezone.now()
    )
    def __str__(self):
        return self.boss