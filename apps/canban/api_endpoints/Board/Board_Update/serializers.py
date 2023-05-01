from rest_framework import serializers

from apps.canban.models import Board


class BoardUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = ['title']
