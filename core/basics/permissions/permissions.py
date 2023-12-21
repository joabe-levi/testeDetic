from rest_framework import permissions


class IsPolicialOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        user = request.user
        if not hasattr(user, 'pessoa'):
            return False
        if user.is_authenticated and user.pessoa.eh_policial:
            return True
        return False
