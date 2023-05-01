from rest_framework.serializers import ModelSerializer

from apps.canban.api_endpoints.Column.Column_List.serializers import ColumnListSerializer
from apps.canban.models import Board


class BoardRetrieveSerializer(ModelSerializer):
    columns = ColumnListSerializer(many=True, read_only=False)

    class Meta:
        model = Board
        fields = ['pk', 'title', 'columns']
