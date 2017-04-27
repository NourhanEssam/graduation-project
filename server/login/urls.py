from django.conf.urls import url
from . import views

app_name = 'login'

urlpatterns = [
    url(r'^$', views.index, name='login'),
    url(r'^login/$', views.index, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
]