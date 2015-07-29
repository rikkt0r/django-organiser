from django.contrib import admin

from .models import Task
from .models import TaskFile
from .models import TaskLog


class TaskAdmin(admin.ModelAdmin):

    readonly_fields = ('date_created', 'date_modified')

    list_display = ('id', 'user', 'date_created', 'public', 'status')

    fieldsets = [
        ('General',     {'fields': ['name', 'description', 'priority', 'user']}),
        ('Location',    {'fields': ['lat', 'lng', 'place_desc']}),
        ('Dates',       {'fields': ['date_created', 'date_modified', 'date_from', 'date_to']}),
        ('Repeat',      {'fields': ['repeat', 'repeat_days']}),
        ('Status',      {'fields': ['public', 'status']})
    ]


class TaskFileAdmin(admin.ModelAdmin):

    readonly_fields = ('id', 'date_created')

    list_display = ('id', 'id', 'type', 'size', 'date_created', 'status')

    fieldsets = [
        ('General',         {'fields': ['id', 'task']}),
        ('Descriptions',    {'fields': ['type', 'size', 'name']}),
        ('Dates, status',   {'fields': ['status', 'date_created']}),
        ('File',            {'fields': ['file']})
    ]


class TaskLogAdmin(admin.ModelAdmin):

    readonly_fields = ('id', 'task', 'date_created')

    list_display = ('id', 'task', 'date_created', 'status')

    fieldsets = [
        ('General',         {'fields': ['id', 'task']}),
        ('Dates created',   {'fields': ['date_created']}),
        ('Description',     {'fields': ['description']}),
    ]

admin.site.register(Task, TaskAdmin)
admin.site.register(TaskFile, TaskFileAdmin)
admin.site.register(TaskLog, TaskLogAdmin)
