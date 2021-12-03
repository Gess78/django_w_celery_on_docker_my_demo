from django.urls import path

from app_0.views import download_pic, index

urlpatterns = [
    path('', index, name='index'),
    path('get_pic/', download_pic, name='download_pic'),
]
