from django.db import models

# Create your models here.
class Likes(models.Model):
    label = models.CharField(max_length=255)

class LikedItem(models.Model):
    like = models.ForeignKey(Likes, on_delete=models.CASCADE)
