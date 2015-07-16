from django.contrib import admin

from .models import Task
from .models import TaskFile
from .models import TaskLog


class TaskAdmin(admin.ModelAdmin):

    readonly_fields = ('date_created', 'date_modified')

    list_display = ('task_id', 'user_id', 'date_created', 'public', 'status')

    fieldsets = [
        ('General',     {'fields': ['name', 'description', 'priority', 'user_id']}),
        ('Location',    {'fields': ['lat', 'lng', 'place_desc']}),
        ('Dates',       {'fields': ['date_created', 'date_modified', 'date_from', 'date_to']}),
        ('Repeat',      {'fields': ['repeat', 'repeat_days']}),
        ('Status',      {'fields': ['public', 'status']})
    ]


class TaskFileAdmin(admin.ModelAdmin):

    readonly_fields = ('task_file_id', 'date_created')

    list_display = ('task_file_id', 'task_id', 'type', 'size', 'date_created', 'status')

    fieldsets = [
        ('General',         {'fields': ['task_file_id', 'task_id']}),
        ('Descriptions',    {'fields': ['type', 'size', 'name']}),
        ('Dates, status',   {'fields': ['status', 'date_created']}),
        ('File',            {'fields': ['file']})
    ]


class TaskLogAdmin(admin.ModelAdmin):

    readonly_fields = ('task_log_id', 'task_id', 'date_created')

    list_display = ('task_log_id', 'task_id', 'date_created', 'status')

    fieldsets = [
        ('General',         {'fields': ['task_log_id', 'task_id']}),
        ('Dates created',   {'fields': ['date_created']}),
        ('Description',     {'fields': ['description']}),
    ]

admin.site.register(Task, TaskAdmin)
admin.site.register(TaskFile, TaskFileAdmin)
admin.site.register(TaskLog, TaskLogAdmin)
