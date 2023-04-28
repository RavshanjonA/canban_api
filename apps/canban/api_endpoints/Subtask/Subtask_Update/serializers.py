from rest_framework import serializers

from apps.canban.models import Subtask


class SubtaskUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subtask
        fields = ['title']
