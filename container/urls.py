from django.urls import path
from . import views

urlpatterns = [
    path('running_containers', views.getData),
    path('execute', views.executeExploit),
    path('execute1', views.executeExploit1),
    path('pid_sh', views.executePIDshell),
    path('expose_host_file', views.executeExposeHostFp),
    path('executeStressTest', views.executeStressTest),
    path('executeShowHashes', views.executeShowHashes),

]
