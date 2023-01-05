from django.db import models

from taggit.managers import TaggableManager


class University(models.Model):
    """
    University model

     Attributes:
        name: A CharField name of a University.
        description: A TextField description of a University.
        datetime_created: A DateTimeField indicating date of creation.
        tags: A TaggableManager tags of a University.
    """

    name = models.CharField(max_length=512, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    datetime_created = models.DateTimeField(
        verbose_name="Дата добавления", null=False, auto_now_add=True
    )

    tags = TaggableManager()

    def __str__(self):
        return f"University<{self.pk}> - {self.name}"

    class Meta:
        verbose_name = "Университет"
        verbose_name_plural = "Университеты"


class Department(models.Model):
    """
    Department model

     Attributes:
        name: A CharField name of a Department.
        datetime_created: A DateTimeField indicating date of creation.
        university: A ForeignKey to University.
    """

    name = models.CharField(max_length=512, null=False, blank=False)
    code = models.CharField(max_length=512, null=False, blank=False)

    university = models.ForeignKey(
        University, on_delete=models.CASCADE, related_name="departments"
    )

    datetime_created = models.DateTimeField(
        verbose_name="Дата добавления", null=False, auto_now_add=True
    )
    # subjects_set = models.PositiveSmallIntegerField(
    #     choices=VERBOSE_SUBJECT_SETS,
    #     default=get_default_subjects_set,
    # )

    tags = TaggableManager()

    def __str__(self):
        return f"Department<{self.pk}> - {self.name}"

    class Meta:
        verbose_name = "Направление"
        verbose_name_plural = "Направления"


class Specialization(models.Model):
    """
    Specialization model

     Attributes:
        name: A CharField name of a Specialization.
        datetime_created: A DateTimeField indicating date of creation.
        department: A ForeignKey to a Department.
        description: A TextField description of a Specialization.
    """

    name = models.CharField(max_length=512, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name="specializations",
    )
    datetime_created = models.DateTimeField(
        verbose_name="Дата добавления", null=False, auto_now_add=True
    )

    tags = TaggableManager()

    def __str__(self):
        return f"Specialization<{self.pk}> - {self.name}"

    class Meta:
        verbose_name = "Специализация"
        verbose_name_plural = "Специализации"
