from django.urls import path

from todolist.views import index

app_name = "todolist"

urlpatterns = [
    path("", index, name="list-tasks"),

]