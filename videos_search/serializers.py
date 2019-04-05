from rest_framework import serializers
from videos_search.models import Video


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ("id","title", "description", 'video_id' ,'title' , "channel_id",'channel_title','published_at')