from rest_framework.serializers import ModelSerializer

from apps.canban.models import Task


class TaskCreateSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
