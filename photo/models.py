from django.db import models

from user.models import User


# Create your models here.
class Photo(models.Model):
    image = models.ImageField(upload_to="photos/")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    caption = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.caption
