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
    path("todolist/create-task/", TaskCreateView.as_view(), name='create-task'),
    path("todolist/<int:pk>/update/", TaskUpdateView.as_view(), name='update-task'),
    path("todolist/<int:pk>/delete/", TaskDeleteView.as_view(), name='delete-task'),


]