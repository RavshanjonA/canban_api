from rest_framework import serializers

from apps.canban.models import Column


class ColumnUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Column
        fields = ['title']
