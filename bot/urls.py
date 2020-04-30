from django.urls import path
from .views import webhook
from .telegram.params import *

app_name = 'telegram_bot'

urlpatterns = [
    path(f'{TOKEN}/',webhook),
#    path(f'{TOKEN}/',webhook,name='web_hook'),
] 
