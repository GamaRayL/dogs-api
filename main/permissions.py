from rest_framework.permissions import BasePermission

from users.models import UserRoles


class IsDogOwner(BasePermission):
    message = 'Вы не являетесь владельцем!'

    def has_object_permission(self, request, view, obj):
        if request.user == obj.owner:
            return True
        return False


class IsDogPublic(BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.is_public


class IsModerator(BasePermission):
    message = 'Вы не являетесь модератором!'

    def has_permission(self, request, view):
        if request.user.role == UserRoles.MODERATOR:
            return True
        return False
