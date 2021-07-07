from django.db import models
from django.utils import timezone

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    summary = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    def body(self):
        return self.summary[:100]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')
