from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

from core.basics.permissions.permissions import IsPolicialOrReadOnly

from rest_framework import permissions


class BasicModelViewSet(ModelViewSet):
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    # permission_classes = [IsPolicialOrReadOnly]
    permission_classes = [permissions.AllowAny]
