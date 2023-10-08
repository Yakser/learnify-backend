from django.contrib.auth import get_user_model
from django.db.models import Q
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

    @classmethod
    def filter_by_fullname(cls, queryset, name, value):
        words = value.split()
        first_word = words[0]
        if len(words) >= 2:
            # if there are more than 2 words, we assume that the first two are first_name and last_name
            first_word, second_word = words[0], words[1]
            # we search for both first_name and last_name in both orders
            return queryset.filter(
                Q(first_name__icontains=first_word)
                | Q(last_name__icontains=second_word)
                | Q(first_name__icontains=second_word)
                | Q(last_name__icontains=first_word)
            )
        return queryset.filter(
            Q(first_name__icontains=first_word) | Q(last_name__icontains=first_word)
        )

    username__contains = filters.Filter(field_name="username", lookup_expr="contains")
    first_name__contains = filters.Filter(
        field_name="first_name", lookup_expr="contains"
    )
    last_name__contains = filters.Filter(field_name="last_name", lookup_expr="contains")
    fullname = filters.CharFilter(method="filter_by_fullname")

    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
        )
