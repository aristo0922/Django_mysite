from django.conf.urls import url
from django.urls import path

from . import views
from .views import index

urlpatterns = [
    path('polls/', index, name='index'),
]