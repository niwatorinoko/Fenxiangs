from django.db import models

# Create your models here.
class Post(models.Model):
    description = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    likes_count = models.IntegerField(default=0)