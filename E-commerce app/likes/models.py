from django.db import models
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

class Like(models.Model):
    label = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.label

class LikedItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL , on_delete= models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete= models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()
    like = models.ForeignKey(Like, on_delete=models.CASCADE ,  null = True)