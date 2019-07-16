from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),  
    # localhost:8000/polls
]