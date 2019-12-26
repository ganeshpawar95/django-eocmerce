from django.db import models

# Create your models here.
class Slider(models.Model):
    slider_title=models.CharField(max_length=100)
    slider_dsc=models.CharField(max_length=100)
    slider_image=models.ImageField(upload_to='media')