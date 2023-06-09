from django.contrib.auth import get_user_model
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    RetrieveAPIView,
    ListAPIView,
)
from django_filters import rest_framework as filters
from rest_framework.permissions import IsAuthenticated

from universities.models import University
from universities.serializers import UniversityListSerializer
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


class CurrentUser(RetrieveAPIView):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = UserDetailSerializer

    def get_object(self):
        return self.request.user


class UserFeed(ListAPIView):
    """
    Returns a list of random universities for the current user.
    # todo: recommendation system
    """

    serializer_class = UniversityListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return University.objects.order_by("?")[:10]
