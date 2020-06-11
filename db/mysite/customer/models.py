from django.db import models

# Create your models here.
class Customer(models.Model):
    name=models.CharField(max_length=200,blank=False)
    sex=models.CharField(max_length=200,blank=False)
    tell=models.CharField(max_length=200,blank=False)
    mail=models.EmailField()
    def __str__(self):
        return self.name
    