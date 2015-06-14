from django.contrib import admin

from .models import User
from .models import Task
from .models import TaskFile

class UserAdmin(admin.ModelAdmin):

    readonly_fields = ('date_created',)

    list_display = ('user_id', 'email', 'date_created')

    fieldsets = [
        ('General',     {'fields': ['name', 'email']}),
        ('Password',    {'fields': ['password']}),
        ('Dates',       {'fields': ['date_created', 'date_logged']})
    ]


# class Task(models.Model):
#     task_id = models.AutoField(primary_key=True)
#     user_id = models.ForeignKey(User)
#     name = models.CharField(max_length=80)
#     description = models.TextField(max_length=1000)
#     date_created = models.DateTimeField(auto_now_add=True)
#     date_from = models.DateTimeField()
#     date_to = models.DateTimeField()
#     amortisation = models.PositiveSmallIntegerField()
#     postpone_count = models.PositiveSmallIntegerField()
#     repeat = models.PositiveSmallIntegerField()
#     lat = models.DecimalField(max_digits=8, decimal_places=6)
#     lng = models.DecimalField(max_digits=8, decimal_places=6)
#     public = models.BooleanField(default=False)
#     status = models.PositiveSmallIntegerField(default=1)
#
#
# class TaskFile(models.Model):
#     task_file_id = models.AutoField(primary_key=True)
#     task_id = models.ForeignKey(Task)
#     file = models.FileField()
#     type = models.CharField(max_length=15)
#     size = models.IntegerField()
#     name = models.CharField(max_length=60, null=True)


admin.site.register(User, UserAdmin)
admin.site.register(Task)
admin.site.register(TaskFile)
