from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.title
    date = models.date
    summary = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
