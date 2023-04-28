from modeltranslation.translator import translator, TranslationOptions

from apps.canban.models import Board, Column, Task, Subtask


# for Person model
class BoardTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


translator.register(Board, BoardTranslationOptions)


class ColumnTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


translator.register(Column, ColumnTranslationOptions)


class TaskTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


translator.register(Task, TaskTranslationOptions)


class SubtaskTranslationOptions(TranslationOptions):
    fields = ('title',)


translator.register(Subtask, SubtaskTranslationOptions)
