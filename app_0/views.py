from django.shortcuts import render, redirect

from app_0 import tasks


def index(request):
    return render(request, 'app_0/index.html')


def download_pic(request):
    tasks.download_pic.delay()
    return redirect('index')
