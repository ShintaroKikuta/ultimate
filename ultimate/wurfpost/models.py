from django.db import models

from django.urls import reverse
# Create your models here.
class Wurfpost(models.Model):
    title = models.CharField(max_length=60)
    datetime = models.DateTimeField()
    description = models.TextField(max_length=10000, default="")
    
    class Meta:
        ordering = ['-datetime']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('wurfpost')
