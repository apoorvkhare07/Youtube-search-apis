from django.urls import path
import videos_search.views as views

urlpatterns = [
    path('',views.VideoListView.as_view(), name='video-list-view'),
    path('api/',views.ApiListView, name='video-list-api')
]