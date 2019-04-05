from django.shortcuts import render
from rest_framework import generics
from .models import Video
from django.http.response import JsonResponse
import requests 
import json
from .serializers import VideoSerializer
from django.views.generic import ListView, CreateView, UpdateView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from cursor_pagination import CursorPaginator

class VideoListView(ListView):
    model = Video
    template_name = "api/video_list.html"
    paginate_by = 12

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        list_video = Video.objects.all().order_by('-published_at')
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
    params=request.GET
    queryset = Video.objects.all().order_by('-published_at')
    page_size = 10
    paginator = CursorPaginator(queryset, ordering=['-id'])
    if 'before' in params:
        before = params['before'] 
        page = paginator.page(first=page_size, before=before)
    elif 'after' in params: 
        after = params['after']
        page = paginator.page(first=page_size, after=after)
    else:
        page = paginator.page(first=page_size, after=None)
    data = {
        'objects': [VideoSerializer(p).data for p in page],
        'has_next_page': page.has_next,
        'has_previous_page': page.has_previous,
        'last_cursor': paginator.cursor(page[-1]),
        'first_cursor': paginator.cursor(page[0])
    }
    return JsonResponse(data)