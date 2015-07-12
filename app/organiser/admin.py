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


class TaskAdmin(admin.ModelAdmin):

    readonly_fields = ('date_created',)

    list_display = ('task_id', 'user_id', 'name', 'date_created')

    fieldsets = [
        ('General',         {'fields': ['name', 'description']}),
        ('Dates',           {'fields': ['date_created', 'date_from', 'date_to']}),
        ('Date details',    {'fields': ['amortisation', 'postpone_count']}),
        ('Coordinates',     {'fields': ['lat', 'lng']}),
        ('Status',     {'fields': ['public', 'status']})
    ]


class TaskFileAdmin(admin.ModelAdmin):

    readonly_fields = ('date_created',)

    list_display = ('task_file_id', 'task_id', 'type', 'date_created')

    fieldsets = [
        ('General',         {'fields': ['name', 'description']}),
        ('Dates',           {'fields': ['date_created', 'date_from', 'date_to']}),
        ('Date details',    {'fields': ['amortisation', 'postpone_count']}),
        ('Coordinates',     {'fields': ['lat', 'lng']}),
        ('Status',     {'fields': ['status']})
    ]
# class TaskFile(models.Model):
#     task_file_id = models.AutoField(primary_key=True)
#     task_id = models.ForeignKey(Task)
#     file = models.FileField()
#     type = models.CharField(max_length=15)
#     size = models.IntegerField()
#     name = models.CharField(max_length=60, null=True)


admin.site.register(User, UserAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(TaskFile)
