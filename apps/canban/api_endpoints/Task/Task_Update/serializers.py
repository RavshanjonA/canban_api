from rest_framework import serializers

from apps.canban.models import Task


class TaskUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['title', 'description', 'subtasks']
        # todo Subtasks nested serializer
