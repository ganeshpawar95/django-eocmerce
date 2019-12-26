from django.db import models

# Create your models here.
class Product(models.Model):
    pro_title=models.CharField(max_length=100)
    product_desc=models.CharField(max_length=1000)
    cat_name=models.CharField(max_length=100)
    bran_name=models.CharField(max_length=100)
    price=models.IntegerField(max_length=100,default="1")
    quantity=models.IntegerField(max_length=100,default="")
    status=models.CharField(max_length=100)
    image=models.ImageField(upload_to='')