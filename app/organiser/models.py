from django.db import models
from django.utils.datetime_safe import datetime


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=26)
    email = models.CharField(max_length=60)
    password = models.CharField(max_length=32)
    date_created = models.DateTimeField(auto_now_add=True)
    date_logged = models.DateTimeField(default=datetime.now, blank=True)


class Task(models.Model):
    task_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User)
    name = models.CharField(max_length=80)
    description = models.TextField(max_length=1000)
    date_created = models.DateTimeField(auto_now_add=True)
    date_from = models.DateTimeField()
    date_to = models.DateTimeField()
    amortisation = models.PositiveSmallIntegerField()
    postpone_count = models.PositiveSmallIntegerField()
    repeat = models.PositiveSmallIntegerField()
    lat = models.DecimalField(max_digits=8, decimal_places=6)
    lng = models.DecimalField(max_digits=8, decimal_places=6)
    public = models.BooleanField(default=False)
    status = models.PositiveSmallIntegerField(default=1, choices=(
        (0, "Removed"),
        (1, "Inactive"),
        (2, "Active"),
        (3, "Done"),
        (4, "Repeated")
    ))


class TaskFile(models.Model):
    task_file_id = models.AutoField(primary_key=True)
    task_id = models.ForeignKey(Task)
    file = models.FileField()
    type = models.CharField(max_length=15)
    size = models.IntegerField()
    name = models.CharField(max_length=60, null=True)
