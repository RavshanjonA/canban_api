from django.db import models
from django.db.models import CharField, TextField, ForeignKey, CASCADE

from apps.common.models import BaseModel


class Board(BaseModel):
    name = CharField(max_length=256)
    description = TextField(null=True, blank=True)

    class Meta:
        db_table = 'board'
        verbose_name = "Board"
        verbose_name_plural = "Boards"


class Status(BaseModel):
    board = ForeignKey('canban.Board', CASCADE, 'status')
    name = CharField(max_length=256)
    description = TextField(null=True, blank=True)

    class Meta:
        db_table = 'ststus'
        verbose_name = 'Status'
        verbose_name_plural = 'Status'


class Task(BaseModel):
    status = ForeignKey('canban.Status', CASCADE, 'tasks')
    title = CharField(max_length=256)
    description = TextField(null=True, blank=True)

    class Meta:
        db_table = 'task'
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'


class Subtask(BaseModel):
    task = ForeignKey('canban.Task', CASCADE, 'subtasks')
    title = CharField(max_length=256)
    description = TextField(null=True, blank=True)

    class Meta:
        db_table = 'subtask'
        verbose_name = "Subtask"
        verbose_name_plural = 'Subtasks'
