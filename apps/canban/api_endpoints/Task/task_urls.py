from django.urls import path

from .Task_Create.views import TaskCreateAPIView
from .Task_Destroy.views import TaskDestroyAPIView
from .Task_List.views import TaskListAPIView
from .Task_Update.views import TaskUpdateAPIView

task_urlpatterns = [
    path('tasks/create/', TaskCreateAPIView.as_view(), name='tasks_create'),
    path('tasks/<int:column_id>/', TaskListAPIView.as_view(), name='tasks_list_by_column'),
    path('tasks/update/<int:pk>/', TaskUpdateAPIView.as_view(), name='tasks_update'),
    path('tasks/destroy/<int:pk>/', TaskDestroyAPIView.as_view(), name='tasks_destroy'),
]
