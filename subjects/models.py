from django.db import models


class Subject(models.Model):
    """
    Subject model

     Attributes:
        name: A CharField name of a Subject.
        datetime_created: A DateTimeField indicating date of creation.
    """

    name = models.CharField(
        max_length=512, null=False, blank=False, verbose_name="Название"
    )
    datetime_created = models.DateTimeField(
        null=False,
        auto_now_add=True,
        verbose_name="Дата добавления",
    )

    def __str__(self):
        return f"Subject<{self.pk}> - {self.name}"

    class Meta:
        verbose_name = "Предмет"
        verbose_name_plural = "Предметы"
