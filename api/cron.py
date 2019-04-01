from django.shortcuts import render
from rest_framework import generics
from videos_search.models import Video
from django.http.response import JsonResponse
import requests 
import json

def youtube_data_cron():
    url = "https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=24&q=ipl&type=video&key=AIzaSyCEWM6z1ayMVnWNyeWLiBrOrBMkF1eLm6I"
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
        existing_videos = Video.objects.all().filter(videoId = videoId)
        if not existing_videos:
            video = Video()
            video.videoId = videoId
            video.title = title
            video.description = description 
            video.channelId = channelId
            video.channelTitle = channelTitle
            video.publishedAt = publishedAt
            video.thumbnailUrl = thumbnailUrl
            video.videoUrl = 'https://www.youtube.com/watch?v='+videoId
            video.save()
    

