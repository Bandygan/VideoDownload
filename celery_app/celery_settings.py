import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'jwt_project.settings')

app = Celery('jwt_project')

app.conf.CELERY_ALWAYS_EAGER = True
app.conf.CELERY_EAGER_PROPAGATES_EXCEPTIONS = True

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()


app.conf.beat_schedule = {
    'add_download_task': {
        'task': 'celery_app.tasks.add_download_task',
        'schedule': 10.0,
    },
    'send_downloaded_torrent': {
        'task': 'celery_app.tasks.send_downloaded_torrent',
        'schedule': 10.0,
    },

}