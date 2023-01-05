from django.db import models

# Create your models here.

from django.utils import timezone

#當django要使用圖片的上船功能時
#要先行安裝 pip install pillow 套件

class Photo(models.Model):
    #upload_to 圖片上船後,存放路徑位置
    #blank,null 這兩個是表示圖片欄位是否可以是空值,False 一定要填
    
    image=models.ImageField(upload_to='images/',blank=False,null=False)
    
    upload_date=models.DateField(default=timezone.now)