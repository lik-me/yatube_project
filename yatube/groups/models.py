from django.db import models

class Group(models.Model):
    title = models.TextField()
    slug = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title