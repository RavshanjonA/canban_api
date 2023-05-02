from rest_framework.serializers import ModelSerializer

from apps.canban.models import Subtask


class SubtaskCreateSerializer(ModelSerializer):
    class Meta:
        model = Subtask
        fields = ['task', 'title']
