from django.db import models


# Create your models here.

class StaticFileExample(models.Model):
    title = models.CharField(max_length=100)
    image = models.FilePathField(path='/img')

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title