from rest_framework.serializers import ModelSerializer

from apps.canban.models import Board


class BoardRetrieveSerializer(ModelSerializer):
    class Meta:
        model = Board
        fields = ['title', 'description', 'pk']  # columns
        # todo column nested serializer for columns field
