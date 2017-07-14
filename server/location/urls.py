from django.conf.urls import url
from . import views

app_name = 'location'

urlpatterns = [
    url(r'^$', views.location, name='location'),
    url(r'^(?P<key>\w+)$', views.location, name='location'),

]
