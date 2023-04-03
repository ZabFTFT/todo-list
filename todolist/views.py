from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic

from todolist.models import Task, Tag


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

class TagListView(generic.ListView):
    model = Tag

class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todolist:list-tag")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todolist:list-tag")

class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("todolist:list-tag")

def switch_complete_status(request, pk: int):
    task = Task.objects.get(id=pk)
    if task.done_marker:
        task.done_marker = False
    else:
        task.done_marker = True
    task.save()
    return redirect("todolist:list-task")




