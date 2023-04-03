from django.db import models


class Tag:
    name = models.CharField(max_length=63)


class Task(models.Model):
    content = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True)
    done_marker = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag)



