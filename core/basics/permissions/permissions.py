from rest_framework import permissions


class BasicPermission(permissions.BasePermission):
    REQUEST_METHODS_TO_READY = ('GET', 'HEAD', 'OPTIONS')

    def has_permission(self, request, view):
        if request.method in self.REQUEST_METHODS_TO_READY:
            return True


class IsPolicialOrReadOnly(BasicPermission):

    def has_permission(self, request, view):
        super().has_permission(request, view)

        user = request.user
        if not hasattr(user, 'pessoa'):
            return False
        return user.is_authenticated and user.pessoa.eh_policial


class IsSuperUserOrReadOnly(BasicPermission):

    def has_permission(self, request, view):
        super().has_permission(request, view)

        user = request.user
        if not hasattr(user, 'pessoa'):
            return False
        return user.is_authenticated and user.is_superuser
