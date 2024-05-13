from django.shortcuts import render
from pytube import YouTube
from django.http import HttpResponse
import requests

def get_link(url):
    ytobject = YouTube(url)
    both = ytobject.streams.get_highest_resolution()
    audio_stream = ytobject.streams.filter(only_audio=True)
    audio_stream = audio_stream[0]
    video_stream = ytobject.streams.filter(only_video=True)
    video_stream = video_stream[0]

    download_links = {"Video & Audio": both.url, "Only Audio": audio_stream.url, "Only Video": video_stream.url}
    name = ytobject.title
    return download_links, name

def download_file(request, url, name, type):
    file_url = url
    if type.lower() == 'video & audio' or type.lower() == 'only video':
        name = name + '.mp4'
    else:
        name = name + '.mp3'
    file_response = HttpResponse()
    file_response['Content-Disposition'] = f'attachment; filename="{name}"'
    file_response['X-Accel-Redirect'] = file_url

    return file_response

# Create your views here.
def home(request):
    if request.method == "POST":
        url = request.POST.get("link")
        download_links, name = get_link(url)
        return render(request, 'base/home.html', {'download_links': download_links, "name":name})
        
    else:
        return render(request, "base/home.html")