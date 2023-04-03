from django.urls import path

from todolist.views import (
    TaskListView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    switch_complete_status,

)

app_name = "todolist"

urlpatterns = [
    path("", TaskListView.as_view(), name="list-task"),
    path("todolist/create-task/", TaskCreateView.as_view(), name='create-task'),
    path("todolist/<int:pk>/update/", TaskUpdateView.as_view(), name='update-task'),
    path("todolist/<int:pk>/delete/", TaskDeleteView.as_view(), name='delete-task'),
    path("todolist/<int:pk>/switch_status/", switch_complete_status, name="switch-status-task" ),


]