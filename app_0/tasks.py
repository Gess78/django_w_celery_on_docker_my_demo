import uuid

import requests
from celery import shared_task
import random
import string

from app_0.models import MyModel


@shared_task
def create_new_object():
    random_name = ''.join([random.choice(string.ascii_letters) for _ in range(10)])
    new_object = MyModel.objects.create(name=random_name)
    return new_object.name


@shared_task
def download_pic():
    for _ in range(10):
        response = requests.get('https://picsum.photos/2000')
        with open(f'pics/img_{uuid.uuid4()}.jpg', "wb") as out:
            out.write(response.content)
    return True
