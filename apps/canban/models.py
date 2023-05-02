from django.db.models import CharField, TextField, ForeignKey, CASCADE, ManyToManyField
from django.utils.translation import gettext_lazy as _
from rest_framework.fields import EmailField

from apps.common.models import BaseModel


class Collaborator(BaseModel):
    user = ForeignKey('users.User', CASCADE, 'users')
    board = ForeignKey('canban.Board', CASCADE, 'collabrators')

class Board(BaseModel):
    user = ForeignKey(verbose_name=_('Owner user'), to='users.User', related_name='my_boards', on_delete=CASCADE)
    title = CharField(verbose_name=_('Board title'), max_length=256, unique=True)
    description = TextField(verbose_name=_('Description'), null=True, blank=True)
    collabrator = ManyToManyField(to='users.User', related_name='boards', through='canban.Collaborator')
    class Meta:
        verbose_name = _('Board')
        verbose_name_plural = _('Boards')

    def __str__(self):
        return f"Board {self.title}"


class Column(BaseModel):
    board = ForeignKey(verbose_name=_('Parent board'), to='canban.Board', related_name='columns', on_delete=CASCADE)
    title = CharField(verbose_name=_('Column title'), max_length=64, unique=True)
    description = TextField(verbose_name=_('Column description'), null=True, blank=True)

    class Meta:
        verbose_name = _('Column')
        verbose_name_plural = _('Columns')

    def __str__(self):
        return f"Column for the board {self.board.title} {self.title}"


class Task(BaseModel):
    column = ForeignKey(verbose_name=_('Parent column'), to='canban.Column', related_name='tasks', on_delete=CASCADE)
    title = CharField(verbose_name=_('Task title'), max_length=256)
    description = TextField(verbose_name=_('Task description'), null=True, blank=True)

    class Meta:
        verbose_name = _('Task')
        verbose_name_plural = _('Tasks')

    def __str__(self):
        return f"Task {self.id} - {self.title} "


class Subtask(BaseModel):
    task = ForeignKey(verbose_name=_('Subtask'), to='canban.Task', on_delete=CASCADE, related_name='subtasks')
    title = CharField(verbose_name=_('Subtask title'), max_length=256)

    class Meta:
        verbose_name = _('Subtask')
        verbose_name_plural = _('Subtasks')

    def __str__(self):
        return f"Subtask {self.id} - {self.title}"
