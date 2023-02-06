from urllib.parse import urlparse
from django.urls import URLPattern, path

from . import views

urlpatterns ={
    path('',views.welcome,name='welcome'),
    path('user',views.user,name='user')
}