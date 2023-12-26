from rest_framework import permissions


class IsPolicialOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        user = request.user
        if not hasattr(user, 'pessoa'):
            return False
        return user.is_authenticated and user.pessoa.eh_policial


class IsSuperUserOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        user = request.user
        if not hasattr(user, 'pessoa'):
            return False
        return user.is_authenticated and user.is_superuser
