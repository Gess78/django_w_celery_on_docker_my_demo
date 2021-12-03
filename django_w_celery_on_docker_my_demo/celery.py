import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_w_celery_on_docker_my_demo.settings')
app = Celery('django_w_celery_on_docker_my_demo')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'creation-new_object': {
        'task': 'app_0.tasks.create_new_object',
        'schedule': 15.0
        # or look at https://docs.celeryproject.org/en/latest/userguide/periodic-tasks.html?highlight=crontab#crontab-schedules
        # 'schedule': crontab(hour=7, minute=10, day_of_week=2),
    }
}
