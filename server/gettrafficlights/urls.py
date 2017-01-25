from django.conf.urls import url
from . import views

app_name = 'gettrafficlights'

urlpatterns = [
    url(r'^$', views.index, name='gettrafficlights'),
]