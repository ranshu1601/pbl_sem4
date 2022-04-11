from django.db import models

class detail(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='about/images/')
    url = models.URLField(blank=True)


