from django.db import models

from photo.models import Photo
from user.models import User


# Create your models here.
class Like(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    photo = models.ForeignKey(to=Photo, on_delete=models.CASCADE)
