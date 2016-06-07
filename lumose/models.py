from django.db import models


# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Photo(models.Model):
    title = models.CharField(max_length=80)
    description = models.CharField(max_length=200)
    file = models.FileField(upload_to='uploads/')
    tags = models.ManyToManyField(Tag)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


