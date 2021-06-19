from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views
urlpatterns = [
    path('',views.home,name='home'),
    # path('<str:key>/  api',views.api,name='api'),
    path('voice',views.voice,name='voice'),
    path('gather',views.gather,name='gather'),

]