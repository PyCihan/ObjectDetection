from django.db import models

# Create your models here.

class Image(models.Model):
    image = models.ImageField(upload_to='ImageServer/media/images/')
    label = models.CharField(max_length=100)
