from rest_framework import status
from rest_framework.generics import RetrieveAPIView, ListCreateAPIView
from django_filters import rest_framework as filters
from rest_framework.response import Response

from core.permissions import IsStaffOrReadOnly
from universities.filters import (
    UniversityFilter,
    SpecializationFilter,
    DepartmentFilter,
)
from universities.models import University, Specialization, Department
from universities.pagination import ListPagination
from universities.serializers import (
    UniversityListSerializer,
    UniversityDetailSerializer,
    SpecializationListSerializer,
    DepartmentListSerializer,
    DepartmentDetailSerializer,
    SpecializationDetailSerializer,
)


class UniversityList(ListCreateAPIView):
    queryset = University.objects.all()
    serializer_class = UniversityListSerializer
    permission_classes = [IsStaffOrReadOnly]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = UniversityFilter
    pagination_class = ListPagination


class UniversityListPaginationLimit(RetrieveAPIView):
    def get(self, request, *args, **kwargs):
        return Response(
            {"limit": ListPagination.default_limit}, status=status.HTTP_200_OK
        )


class UniversityDetail(RetrieveAPIView):
    queryset = University.objects.all()
    serializer_class = UniversityDetailSerializer
    permission_classes = [IsStaffOrReadOnly]


class DepartmentList(ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentListSerializer
    permission_classes = [IsStaffOrReadOnly]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = DepartmentFilter
    pagination_class = ListPagination


class DepartmentDetail(RetrieveAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentDetailSerializer
    permission_classes = [IsStaffOrReadOnly]


class SpecializationList(ListCreateAPIView):
    queryset = Specialization.objects.applied_or_without_physics()
    serializer_class = SpecializationListSerializer
    permission_classes = [IsStaffOrReadOnly]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = SpecializationFilter
    pagination_class = ListPagination


class SpecializationDetail(RetrieveAPIView):
    queryset = Specialization.objects.all()
    serializer_class = SpecializationDetailSerializer
    permission_classes = [IsStaffOrReadOnly]


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
