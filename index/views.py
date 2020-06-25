#index的view.py

from django.shortcuts import render, HttpResponse
from .models import *
# Create your views here.


def indexView(request):
    # 热搜index.html歌曲
    search_song = Dynamic.objects.select_related("song").order_by('-dynamic_search').all()[0:8]
    # 音乐分类
    label_list = Label.objects.all()
    # 热门歌曲
    play_hot_song = Dynamic.objects.select_related('song').order_by('-dynamic_plays').all()[0:10]
    # 新歌推荐
    daily_recommendation = Song.objects.order_by('-song_release').all()[0:3]
    # 热门搜索，热门下载
    search_ranking = search_song[0:6]
    down_ranking = Dynamic.objects.select_related('song').order_by('-dynamic_down').all()[0:6]
    all_ranking = [search_ranking, down_ranking]
    return render(request, 'index.html', locals())


