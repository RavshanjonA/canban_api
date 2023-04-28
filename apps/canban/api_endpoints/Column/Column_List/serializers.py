from rest_framework.serializers import ModelSerializer

from apps.canban.models import Column


class ColumnListSerializer(ModelSerializer):
    class Meta:
        model = Column
        fields = ['title', 'description']
        # todo add filter by the board the column belongs to
        # todo add Tasks nested serializer
