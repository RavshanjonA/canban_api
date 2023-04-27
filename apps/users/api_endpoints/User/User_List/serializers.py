from rest_framework.serializers import ModelSerializer

from apps.users.models import User


class UserListSerializer(ModelSerializer):
    class Meta:
        model = User
        exclude = ['is_staff', 'is_active', 'is_superuser', 'groups', 'last_login', 'user_permissions']
