from rest_framework.pagination import LimitOffsetPagination


class UniversityListPagination(LimitOffsetPagination):
    default_limit = 6
