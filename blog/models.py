from django.db import models

# Create your models here.

class Blog(models.Model):
    author = models.CharField(max_length = 100)
    title = models.CharField(max_length = 100)
    description = models.TextField()

    def __str__(self):
        return self.author