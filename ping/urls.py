from django.urls import path
from . import views

urlpatterns = [
    path('ping1', views.simple_ping),
    # path('execute', views.executeExploit),
]
