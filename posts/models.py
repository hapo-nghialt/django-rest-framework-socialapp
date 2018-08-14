from django.db import models
from django.conf import settings

class Post(models.Model):
    content = models.TextField()
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.content

    class Meta:
        ordering = ["timestamp", "updated"]
