from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):

    CHOICES = (
        (0, 'Do not repeat'),
        (1, 'Daily'),
        (2, 'Weekly'),
        (4, 'Monthly'),
        (8, 'Other (enter days count)'),
    )

    task_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User)
    name = models.CharField(max_length=80)
    description = models.TextField(max_length=2000)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True, blank=True)
    date_from = models.DateTimeField()
    date_to = models.DateTimeField()
    repeat = models.PositiveSmallIntegerField()
    lat = models.DecimalField(max_digits=8, decimal_places=6)
    lng = models.DecimalField(max_digits=8, decimal_places=6)
    public = models.BooleanField(default=False)
    status = models.PositiveSmallIntegerField(default=1)


class TaskFile(models.Model):
    task_file_id = models.AutoField(primary_key=True)
    task_id = models.ForeignKey(Task)
    file = models.FileField()
    type = models.CharField(max_length=15)
    size = models.IntegerField()
    name = models.CharField(max_length=60, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True, blank=True)


class TaskLog(models.Model):

    task_log_id = models.AutoField(primary_key=True)
    task_id = models.ForeignKey(Task)
    description = models.TextField(max_length=1000)
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True, blank=True)
