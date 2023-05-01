from django.urls import path

from .Subtask_Create.views import SubtaskCreateAPIView
from .Subtask_Destroy.views import SubtaskDestroyAPIView
from .Subtask_List.views import SubtaskListAPIView
from .Subtask_Update.views import SubtaskUpdateAPIView

subtask_urlpatterns = [
    path('subtasks/create/', SubtaskCreateAPIView.as_view(), name='subtasks_create'),
    path('subtasks/<int:task_id>/', SubtaskListAPIView.as_view(), name='subtasks_list_by_task'),
    path('subtasks/update/<int:pk>/', SubtaskUpdateAPIView.as_view(), name='subtasks_update'),
    path('subtasks/destroy/<int:pk>/', SubtaskDestroyAPIView.as_view(), name='subtasks_destroy'),
]
