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

]