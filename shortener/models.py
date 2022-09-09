from django.db import models

class shorten(models.Model):
    url = models.CharField(max_length=250)
    slug = models.CharField(max_length=100)

    def __str__(self):
        return self.url