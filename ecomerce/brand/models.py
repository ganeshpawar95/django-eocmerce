from django.db import models
from shop.models import Category

# Create your models here.
class Brand(models.Model):
    cat_name=models.CharField(max_length=100)
    bran_name=models.CharField(max_length=100)
    def __str__(self):
        return self.bran_name
