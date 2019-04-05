from django.db import models

class Video(models.Model):
    video_id= models.CharField(max_length= 255, null=False)
    title = models.CharField(max_length=255, null= False) 
    description = models.TextField(null=True)
    channel_id = models.CharField(max_length=255, null= False)
    channel_title = models.CharField(max_length=255, null= False)
    video_url = models.CharField(max_length= 511, null = False)
    published_at = models.DateTimeField()
    thumbnail_url = models.CharField(max_length = 511)
    def __str__(self):
        return self.title