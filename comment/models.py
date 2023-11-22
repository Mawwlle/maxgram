from django.db import models

from post.models import Post
from user.models import User


# Create your models here.
class Comment(models.Model):
    content = models.TextField()
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE)
