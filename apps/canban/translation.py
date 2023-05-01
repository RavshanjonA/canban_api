from modeltranslation.translator import translator, TranslationOptions

from apps.canban.models import Board, Column, Task, Subtask


# for Person model
class BoardTranslationOptions(TranslationOptions):
    fields = ('title',)


class ColumnTranslationOptions(TranslationOptions):
    fields = ('title',)


class TaskTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


class SubtaskTranslationOptions(TranslationOptions):
    fields = ('title',)


translator.register(Board, BoardTranslationOptions)
translator.register(Column, ColumnTranslationOptions)
translator.register(Task, TaskTranslationOptions)
translator.register(Subtask, SubtaskTranslationOptions)
