from django.contrib import admin
from apps.canban.models import Board, Column, Task, Subtask
# Register your models here.

admin.site.register(Board)
admin.site.register(Column)
admin.site.register(Task)
admin.site.register(Subtask)
