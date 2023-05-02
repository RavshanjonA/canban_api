from rest_framework.serializers import ModelSerializer

from apps.canban.api_endpoints.Task.Task_List.serializers import TaskListSerializer
from apps.canban.models import Column


class ColumnListSerializer(ModelSerializer):
    tasks = TaskListSerializer(many=True, read_only=False)

    class Meta:
        model = Column
        fields = ['id', 'title', 'tasks']
