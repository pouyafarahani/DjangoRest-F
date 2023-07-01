from django.db import models


class BlogModel(models.Model):

    title = models.CharField(max_length=255)
    time_create = models.DateTimeField(auto_now_add=True)
    body = models.TextField()