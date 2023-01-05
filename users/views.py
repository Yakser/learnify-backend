from django.contrib.auth import get_user_model
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from django_filters import rest_framework as filters
from rest_framework.permissions import IsAuthenticated

from users.filters import UserFilter
from users.permissions import IsMyselfOrReadOnly
from users.serializers import UserListSerializer, UserDetailSerializer

User = get_user_model()


class UserList(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = UserFilter


class UserDetail(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    permission_classes = [IsMyselfOrReadOnly, IsAuthenticated]
    serializer_class = UserDetailSerializer
