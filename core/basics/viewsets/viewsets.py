from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import status
from rest_framework.response import Response

from core.basics.permissions.permissions import IsPolicialOrReadOnly


class BasicModelViewSet(ModelViewSet):
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    permission_classes = [IsPolicialOrReadOnly]
    perform_destroy = False

    def get_perform_destroy(self):
        return self.perform_destroy

    def destroy(self, request, *args, **kwargs):
        if self.get_perform_destroy():
            return super().destroy(request, *args, **kwargs)

        instance = self.get_object()
        instance.ativo = False
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
