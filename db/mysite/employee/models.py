from django.db import models
from boss.models import Boss
# Create your models here.
class Employee(models.Model):
    name=models.CharField(max_length=200,blank=False)
    salary=models.PositiveIntegerField()
    job_title=models.CharField(max_length=200,blank=False)
    tell=models.CharField(max_length=200,blank=False)
    mail=models.EmailField()
    published_date = models.DateTimeField(
      blank=True, null=True
    )
    boss=models.ForeignKey('boss.Boss', on_delete=models.CASCADE)

    def __str__(self):
        return self.name