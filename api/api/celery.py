import os

from celery import Celery

CELERY_BROKER_URL = os.getenv('DJANGO_CELERY_BROKER_URL', 'redis://localhost:6379/0')
CELERY_RESULT_BACKEND = os.getenv('CELERY_RESULT_BACKEND', 'rpc://')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api.settings')

app = Celery(
    'api',
    broker = CELERY_BROKER_URL,
    backend = CELERY_RESULT_BACKEND

)
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')