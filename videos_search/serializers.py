from rest_framework import serializers
from videos_search.models import Video


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ("title", "description", 'videoId' ,'title' ,"description", "channelId",'channelTitle','publishedAt')