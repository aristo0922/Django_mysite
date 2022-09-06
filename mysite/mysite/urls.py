from django.conf.urls import include
from django.contrib import admin
from django.urls import path

from account.views import UsertListAPI

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('api/user/', UsertListAPI.as_view())
]