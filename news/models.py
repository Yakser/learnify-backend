from django.db import models
from simple_history.models import HistoricalRecords
from taggit.managers import TaggableManager


class News(models.Model):
    """
    News model

    Attributes:
        title: A CharField title of News.
        text: A TextField text of News.
        created_at: A DateTimeField created_at of News.
        updated_at: A DateTimeField updated_at of News.
    """

    title = models.TextField(
        null=False,
        blank=False,
        verbose_name="Заголовок",
    )
    text = models.TextField(null=False, blank=False, verbose_name="Текст")
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата обновления",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания",
    )
    categories = models.ManyToManyField(
        "Category",
        related_name="news",
        verbose_name="Категории",
        help_text='Например: "Образование", "Технологии" и т.д.',
    )

    history = HistoricalRecords()
    tags = TaggableManager()

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"

    def __str__(self):
        return f"News<{self.pk}> - {self.title}"


class Category(models.Model):
    """
    Category model

    Attributes:
        title: A CharField title of Category.
        slug: A SlugField slug of Category.
        description: A TextField description of Category.
        created_at: A DateTimeField created_at of Category.
        updated_at: A DateTimeField updated_at of Category.
    """

    title = models.CharField(
        max_length=255,
        null=False,
        blank=False,
        verbose_name="Название",
    )
    slug = models.SlugField(
        max_length=255,
        null=False,
        blank=False,
        verbose_name="Слаг",
    )
    description = models.TextField(
        null=True,
        blank=True,
        verbose_name="Описание",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата обновления",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания",
    )
    history = HistoricalRecords()

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return f"Category<{self.pk}> - {self.title}"
