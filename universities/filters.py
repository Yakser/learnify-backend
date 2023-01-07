from django_filters import rest_framework as filters

from universities.models import University, Specialization, Department


def filter_by_tags(queryset, name, value):
    tags = value
    if tags:
        tags = tags.split(",")
        queryset = queryset.filter(tags__name__in=tags).distinct()

    return queryset


class UniversityFilter(filters.FilterSet):
    """
    Filter for Universities

    Adds filtering to DRF list retrieve views
    Parameters to filter by:
        name (str)
        city (str)
        tags (str)
    Examples:
        ?name=test equals to .filter(name='test')
        ?tags=tag1,tag2 equals to .filter(tags__name__in=tags).distinct()
        ?name__contains=yawning equals to .filter(name__contains='yawning')
    """

    name__contains = filters.Filter(field_name="name", lookup_expr="contains")
    tags = filters.CharFilter(
        field_name="tags__name",
        method=filter_by_tags,
    )

    class Meta:
        model = University
        fields = (
            "name",
            "city",
            "tags",
        )


class SpecializationFilter(filters.FilterSet):
    """
    Filter for Specializations

    Adds filtering to DRF list retrieve views
    Parameters to filter by:
        name (str)
    Examples:
        ?name=test equals to .filter(name='test')
        ?name__contains=yawning equals to .filter(name__contains='yawning')
    """

    name__contains = filters.Filter(field_name="name", lookup_expr="contains")
    tags = filters.CharFilter(
        field_name="tags__name",
        method=filter_by_tags,
    )

    class Meta:
        model = Specialization
        fields = (
            "name",
            "tags",
        )


class DepartmentFilter(filters.FilterSet):
    """
    Filter for Departments

    Adds filtering to DRF list retrieve views
    Parameters to filter by:
        name (str)
    Examples:
        ?name=test equals to .filter(name='test')
        ?name__contains=yawning equals to .filter(name__contains='yawning')
    """

    name__contains = filters.Filter(field_name="name", lookup_expr="contains")
    tags = filters.CharFilter(
        field_name="tags__name",
        method=filter_by_tags,
    )

    class Meta:
        model = Department
        fields = (
            "name",
            "tags",
        )
