from rest_framework import permissions


class IsPolicialOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        if not hasattr(request.user, 'pessoa'):
            return False
        if request.user.is_authenticated and request.user.pessoa.eh_policial:
            return True
        return False
