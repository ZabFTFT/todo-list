from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from todolist.models import Task


class TaskListView(generic.ListView):
    model = Task
    queryset = Task.objects.prefetch_related("tags")


class TaskCreateView(generic.CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("todolist:list-task")


class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("todolist:list-task")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("todolist:list-task")


