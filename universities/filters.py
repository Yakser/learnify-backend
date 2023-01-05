from django_filters import rest_framework as filters

from universities.models import University


class UniversityFilter(filters.FilterSet):
    """
    Filter for Universities

    Adds filtering to DRF list retrieve views
    Parameters to filter by:
        name (str)
    Examples:
        ?name=test equals to .filter(name='test')
        ?name__contains=yawning equals to .filter(name__contains='yawning')
    """

    name__contains = filters.Filter(field_name="name", lookup_expr="contains")

    class Meta:
        model = University
        fields = ("name",)
