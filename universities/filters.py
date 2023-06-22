from django_filters import rest_framework as filters

from universities.models import University, Specialization, Department


def filter_by_tags(queryset, name, value):
    if value:
        tags = value.split(",")
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

    name__icontains = filters.Filter(field_name="name", lookup_expr="icontains")
    city = filters.CharFilter(
        field_name="city",
        lookup_expr="iexact",
    )
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

    name__icontains = filters.Filter(field_name="name", lookup_expr="icontains")
    tags = filters.CharFilter(
        field_name="tags__name",
        method=filter_by_tags,
    )

    city = filters.CharFilter(
        field_name="department__university__city",
        lookup_expr="iexact",
    )

    class Meta:
        model = Specialization
        fields = ("name", "tags", "city")


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

    name__icontains = filters.Filter(field_name="name", lookup_expr="icontains")
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
