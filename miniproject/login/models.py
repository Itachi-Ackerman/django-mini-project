from django.db import models

# Create your models here.
class uploads(models.Model):
    objects=None
    pic=models.ImageField(upload_to='pics/')