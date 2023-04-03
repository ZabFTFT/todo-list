from django.urls import path

from todolist.views import (
    TaskListView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
)

app_name = "todolist"

urlpatterns = [
    path("", TaskListView.as_view(), name="list-task"),
    path("create-task/", TaskCreateView.as_view(), name='create-task'),


]