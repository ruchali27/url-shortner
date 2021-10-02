from django.db import models

# Create your models here.

class Url(models.Model):
    url=models.CharField(max_length=100)
    short_url=models.CharField(max_length=15)

    def __str__(self):
        return self.short_url

