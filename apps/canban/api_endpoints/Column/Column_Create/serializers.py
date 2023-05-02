from rest_framework.serializers import ModelSerializer

from apps.canban.models import Column


class ColumnCreateSerializer(ModelSerializer):
    class Meta:
        model = Column
        fields = ['title', 'board']
