from django.db import models
import storages.backends.s3boto


protected_storage = storages.backends.s3boto.S3BotoStorage(
    acl='private',
    querystring_auth=True,
    querystring_expire=600
)


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
    file = models.FileField(
        storage=protected_storage,
        default='./lumose/static/imageNotFound.jpg'
    )
    tags = models.ManyToManyField(Tag)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


