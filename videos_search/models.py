from django.db import models

# Create your models here.
class Video(models.Model):
    videoId= models.CharField(max_length= 255, null=False)
    title = models.CharField(max_length=255, null= False) 
    description = models.TextField(null=True)
    channelId = models.CharField(max_length=255, null= False)
    channelTitle = models.CharField(max_length=255, null= False)
    videoUrl = models.CharField(max_length= 511, null = False)
    publishedAt = models.DateTimeField()
    thumbnailUrl = models.CharField(max_length = 511)
    def __str__(self):
        return self.title