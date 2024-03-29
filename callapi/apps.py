from django.apps import AppConfig
from django.conf import settings

class CallapiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'callapi'
    def ready(self):
        from . import scheduler
        scheduler.start()