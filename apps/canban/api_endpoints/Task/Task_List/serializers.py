from rest_framework.serializers import ModelSerializer

from apps.canban.api_endpoints.Subtask.Subtask_List.serializers import SubtaskListSerializer
from apps.canban.models import Task


class TaskListSerializer(ModelSerializer):
    subtasks = SubtaskListSerializer(many=True, read_only=False)

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'subtasks']
        # todo Subtasks nested serializer
