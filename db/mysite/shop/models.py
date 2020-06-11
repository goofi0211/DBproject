from django.db import models
from django.utils import timezone
import os

# 產品圖片的存放路徑是 media/uploads/xxx.jpg，
# 而存放在 DB 的路徑是 uploads/xxx.jpg
# 所以我們在 html 使用時，需要自己補 /media/ 的前綴
# 在 html 的完整使用是 /media/{product.0.img}
def get_image_path(instance, filename):
    return os.path.join('uploads', filename)
# Create your models here.
class Commodity(models.Model):
    name=models.CharField(max_length=200,blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=0)
    origin=models.CharField(max_length=200)
    stock = models.PositiveIntegerField()
    img = models.ImageField(
      blank=True,
      null=True,
      upload_to=get_image_path, 
      default=get_image_path(
        instance=0, filename='product-1.jpg'
      )
    )
    # for analysis，網頁使用者看不到，但可事後分析的屬性
    
    published_date = models.DateTimeField(
      blank=True, null=True
    )
    
    def publish(self):
        self.published_date = timezone.now
        self.save()

    def __str__(self):
        return self.name