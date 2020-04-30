from django.conf.urls import include, url 
from django.urls import path
from django.contrib import admin
from dataAPI.views import index, post_detail, dashboard

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('projects/get/<last>/<bd>/<bt>/<ed>/<et>',post_detail),#, name='post_detail'),
    path('dashboard/<pk>/<last>/<bd>/<bt>/<ed>/<et>',dashboard),#,name='dashboard'),
    path('telegram_bot/',include('bot.urls','bot'))
]

#    path('/',include('bot.urls','bot'))
# so all url==>/{token}
