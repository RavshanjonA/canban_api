from rest_framework.serializers import ModelSerializer

from apps.canban.models import Task


class TaskRetrieveSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'description']
