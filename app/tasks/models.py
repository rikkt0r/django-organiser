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

    STATUSES = (
        (0, 'Deleted'),
        (1, 'Active'),
        (2, 'Done')
    )

    PRIORITIES = (
        (0, 'No rush'),
        (1, 'Just another task'),
        (2, 'Do it quickly'),
        (3, 'LIFE THREATENING')
    )

    task_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User)
    name = models.CharField(max_length=80)
    description = models.TextField(max_length=2000)
    priority = models.PositiveSmallIntegerField(default=1, choices=PRIORITIES)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True, blank=True)
    date_from = models.DateTimeField()
    date_to = models.DateTimeField()
    repeat = models.PositiveSmallIntegerField(choices=CHOICES)
    repeat_days = models.PositiveSmallIntegerField(default=0)
    lat = models.DecimalField(max_digits=8, decimal_places=6, blank=True, null=True)
    lng = models.DecimalField(max_digits=8, decimal_places=6, blank=True, null=True)
    place_desc = models.CharField(max_length=250, blank=True)
    public = models.BooleanField(default=False)
    status = models.PositiveSmallIntegerField(default=1, choices=STATUSES)

    def __str__(self):
        return "Task ID: " + str(self.task_id)


class TaskFile(models.Model):

    TYPES = (
        (0, 'Unknown'),
        (1, 'Image'),
        (2, 'Audio'),
        (3, 'Video')
    )

    task_file_id = models.AutoField(primary_key=True)
    task_id = models.ForeignKey(Task)
    file = models.FileField()
    type = models.PositiveSmallIntegerField(default=0, choices=TYPES)
    size = models.IntegerField()
    name = models.CharField(max_length=60, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True, blank=True)

    def __str__(self):
        return "File ID: " + str(self.task_file_id)


class TaskLog(models.Model):

    STATUSES = (
        (False, 'Deleted'),
        (True, 'Active')
    )

    task_log_id = models.AutoField(primary_key=True)
    task_id = models.ForeignKey(Task)
    description = models.TextField(max_length=1000)
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True, choices=STATUSES)

    def __str__(self):
        return "Log ID: " + str(self.task_log_id)