from rest_framework.generics import ListAPIView, RetrieveAPIView
from django_filters import rest_framework as filters

from universities.filters import (
    UniversityFilter,
    SpecializationFilter,
    DepartmentFilter,
)
from universities.models import University, Specialization, Department
from universities.serializers import (
    UniversityListSerializer,
    UniversityDetailSerializer,
    SpecializationListSerializer,
    DepartmentListSerializer,
    DepartmentDetailSerializer,
    SpecializationDetailSerializer,
)


class UniversityList(ListAPIView):
    queryset = University.objects.all()
    serializer_class = UniversityListSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = UniversityFilter


class UniversityDetail(RetrieveAPIView):
    queryset = University.objects.all()
    serializer_class = UniversityDetailSerializer


class DepartmentList(ListAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentListSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = DepartmentFilter


class DepartmentDetail(RetrieveAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentDetailSerializer


class SpecializationList(ListAPIView):
    queryset = Specialization.objects.all()
    serializer_class = SpecializationListSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = SpecializationFilter


class SpecializationDetail(RetrieveAPIView):
    queryset = Specialization.objects.all()
    serializer_class = SpecializationDetailSerializer


# class UniversityDepartmentList(ListAPIView):
#     serializer_class = DepartmentListSerializer
#     filter_backends = (filters.DjangoFilterBackend,)
#     filterset_class = DepartmentFilter
#
#     def get_queryset(self):
#         pk = self.kwargs.get("pk")
#         return Department.objects.filter(pk=pk)


# class UniversityDepartmentDetail(RetrieveAPIView):
#     serializer_class = DepartmentDetailSerializer
#
#     def get_queryset(self):
#         department_id = self.kwargs.get("department_id")
#         return Department.objects.filter(pk=department_id)
