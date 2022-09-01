from django.template.defaulttags import url
from django.urls import include, path

from account import admin
from account.views import hello_world

app_name='account'



urlpatterns = [
    path('hello_world/', hello_world, name='hello_world')
]