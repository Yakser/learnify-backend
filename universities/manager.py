from django.db import models
from django.db.models import Q


class SpecializationManager(models.Manager):
    def exclude_university(self, university_pk: int):
        return self.get_queryset().filter(~Q(university__pk=university_pk))

    def applied_or_without_physics(self):
        return self.get_queryset().filter(
            Q(name__icontains="Прикладная")
            | (~Q(name__icontains="физика") & ~Q(name__icontains="физические"))
        )
