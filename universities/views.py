from rest_framework.generics import ListAPIView
from django_filters import rest_framework as filters

from universities.filters import UniversityFilter
from universities.models import University
from universities.serializers import (
    UniversityListSerializer,
    UniversityDetailSerializer,
)


class UniversityList(ListAPIView):
    queryset = University.objects.all()
    serializer_class = UniversityListSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = UniversityFilter


class UniversityDetail(ListAPIView):
    queryset = University.objects.all()
    serializer_class = UniversityDetailSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = UniversityFilter
