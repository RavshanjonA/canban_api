from rest_framework.serializers import ModelSerializer

from apps.canban.models import Board


class BoardCreateSerializer(ModelSerializer):
    class Meta:
        model = Board
        fields = ['title']
