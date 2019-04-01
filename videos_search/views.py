from django.shortcuts import render
from rest_framework import generics
from .models import Video
from django.http.response import JsonResponse
import requests 
import json
from .serializers import VideoSerializer
from django.views.generic import ListView, CreateView, UpdateView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

class VideoListView(ListView):
    model = Video
    template_name = "api/video_list.html"
    paginate_by = 12

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        list_video = Video.objects.all().order_by('-publishedAt')
        paginator = Paginator(list_video, self.paginate_by)

        page = self.request.GET.get('page')

        try:
            videos = paginator.page(page)
        except PageNotAnInteger:
            videos = paginator.page(1)
        except EmptyPage:
            videos = paginator.page(paginator.num_pages)

        context['list_videos'] = videos
        return context

def ApiListView(request):
    pageId = request.GET.get('pageId')
    if not pageId:
        pageId = 1
    index = (int(pageId)-1)*12
    queryset = Video.objects.all().order_by('-publishedAt')[index:index+12]
    query_result = []
    for i in queryset:
        serializer_class = VideoSerializer(i)
        query_result.append(serializer_class.data)
        nextPageId = int(pageId)+1
    return JsonResponse({'query_response':query_result,'nextPageId': nextPageId })
