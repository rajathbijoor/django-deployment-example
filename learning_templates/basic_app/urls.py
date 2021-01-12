from django.conf.urls import url
from basic_app import views

app_name = 'basic_app'

urlpatterns = [
        url(r'^other/$', views.other, name='oth'),
        url(r'^relative/$', views.relative, name='rut'),
]