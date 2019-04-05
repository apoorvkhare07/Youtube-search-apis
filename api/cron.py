from django.shortcuts import render
from rest_framework import generics
from videos_search.models import Video
from django.http.response import JsonResponse
import requests 
import json
from datetime import datetime,timedelta

def youtube_data_cron():
    last_hour = datetime.utcnow() - timedelta(hours = 1)
    published_after = last_hour.isoformat("T")+"Z"
    url = "https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=24&q=how%20to&type=video&order=date&publishedAfter="+ str(published_after)+"&key=AIzaSyCEWM6z1ayMVnWNyeWLiBrOrBMkF1eLm6I"
    response = requests.get(url)
    respons = json.loads(response.content)
    data = []
    for i in respons['items']:
        videoId = i['id']['videoId']
        title = i['snippet']['title']
        description = i['snippet']['description']
        publishedAt = i['snippet']['publishedAt']
        channelId = i['snippet']['channelId']
        channelTitle = i['snippet']['channelTitle']
        thumbnailUrl = i['snippet']['thumbnails']['default']['url']
        existing_videos = Video.objects.all().filter(video_id = videoId)
        if not existing_videos:
            video = Video()
            video.video_id = videoId
            video.title = title
            video.description = description 
            video.channel_id = channelId
            video.channel_title = channelTitle
            video.published_at = publishedAt
            video.thumbnail_url = thumbnailUrl
            video.video_url = 'https://www.youtube.com/watch?v='+videoId
            video.save()
    

