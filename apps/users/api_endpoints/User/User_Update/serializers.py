from rest_framework import serializers

from apps.users.models import User


class UserUpdateSerializer(serializers.ModelSerializer):
    profile_photo = serializers.ImageField(required=False)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'phone_number', 'profile_photo', 'gender']
        # exclude = ['is_staff', 'is_active', 'is_superuser', 'groups', 'last_login', 'user_permissions']
