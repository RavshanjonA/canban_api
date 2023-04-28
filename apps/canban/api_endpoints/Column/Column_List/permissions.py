from rest_framework.permissions import BasePermission


class IsTheOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.board.user == request.user
