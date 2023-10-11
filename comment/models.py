from django.db import models
from photo.models import Photo

from user.models import User


# Create your models here.
class Comment(models.Model):
    content = models.TextField()
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    photo = models.ForeignKey(to=Photo, on_delete=models.CASCADE)
