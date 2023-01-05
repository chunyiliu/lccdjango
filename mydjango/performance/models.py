from django.db import models

# Create your models here.

class Sales(models.Model):
    title=models.CharField(max_length=50)
    info=models.TextField()
    photos=models.CharField(max_length=200)
    link=models.CharField(max_length=200)
    create_date=models.DateField(auto_now_add=True)
    
    class Meta:
        db_table='sales'