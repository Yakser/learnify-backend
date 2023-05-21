from rest_framework.pagination import LimitOffsetPagination


class ListPagination(LimitOffsetPagination):
    default_limit = 6
