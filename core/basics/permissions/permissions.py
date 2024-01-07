from rest_framework import permissions


class BasicPermission(permissions.BasePermission):
    REQUEST_METHODS_TO_ALLOW = ('GET', 'HEAD', 'OPTIONS')

    def has_permission(self, request, view):
        return request.method in self.REQUEST_METHODS_TO_ALLOW


class IsPolicialOrReadOnly(BasicPermission):

    def has_permission(self, request, view):
        if super().has_permission(request, view):
            return True

        user = request.user
        return user.is_authenticated and hasattr(user, 'pessoa') and user.pessoa.eh_policial


class IsSuperUserOrReadOnly(BasicPermission):

    def has_permission(self, request, view):
        if super().has_permission(request, view):
            return True

        user = request.user
        return user.is_authenticated and user.is_superuser
