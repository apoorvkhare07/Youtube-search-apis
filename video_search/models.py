from django.db import models

# Create your models here.
class Video(models.Model):
    videoId= models.CharField(maxlength= 255, null=False)
    title = models.CharField(maxlength=255, null= False) 
    description = models.TextField(null=True)
    channelId = models.CharField(maxlength=255, null= False)
    channelTitle = models.CharField(maxlength=255, null= False)

    def __str__(self):
        return self.title