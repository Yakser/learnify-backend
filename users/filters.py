from django.contrib.auth import get_user_model
from django_filters import rest_framework as filters

User = get_user_model()


class UserFilter(filters.FilterSet):
    """
    Filter for Users
    Adds filtering to DRF list retrieve views
    Parameters to filter by:
        first_name (str), last_name (str), username (str),
    Examples:
        ?first_name=test equals to .filter(first_name='test')
        ?username__contains=yawning equals to .filter(username__contains='yawning')
    """

    username__contains = filters.Filter(field_name="username", lookup_expr="contains")
    first_name__contains = filters.Filter(
        field_name="first_name", lookup_expr="contains"
    )
    last_name__contains = filters.Filter(field_name="last_name", lookup_expr="contains")

    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
        )
