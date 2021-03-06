""" Assignments UrlConf """

from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views

urlpatterns = [
    path('tasks/new/', login_required(views.new_task), name='new_task'),
    path('tasks/', login_required(views.show_tasks), name='show_tasks'),
    path('<int:pk>', login_required(views.update_assignment), name='update_assignment'),
]
