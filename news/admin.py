from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin

from news.models import News, Category


@admin.register(News)
class NewsAdmin(SimpleHistoryAdmin):
    list_display = (
        "id",
        "title",
        "created_at",
    )
    list_display_links = (
        "id",
        "title",
        "created_at",
    )

    search_fields = (
        "id",
        "title",
    )

    date_hierarchy = "created_at"
    list_filter = (
        "created_at",
        "updated_at",
    )
    filter_horizontal = ("categories",)


@admin.register(Category)
class CategoryAdmin(SimpleHistoryAdmin):
    list_display = (
        "id",
        "title",
        "slug",
    )
    list_display_links = (
        "id",
        "title",
        "slug",
    )

    search_fields = (
        "id",
        "title",
        "slug",
    )

    date_hierarchy = "created_at"
    list_filter = (
        "created_at",
        "updated_at",
    )


# admin.site.register(News, SimpleHistoryAdmin)
