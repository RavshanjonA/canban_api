from rest_framework.serializers import ModelSerializer

from apps.canban.models import Subtask


class SubtaskListSerializer(ModelSerializer):
    class Meta:
        model = Subtask
        fields = ['title']
