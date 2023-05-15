from django.urls import path
from . import views

urlpatterns = [
    path('', views.simple_ping),
    # path('execute', views.executeExploit),
]
