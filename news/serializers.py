from rest_framework import serializers

from news.models import News


class NewsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = (
            "id",
            "title",
            "text",
            "created_at",
        )


class NewsDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = (
            "id",
            "title",
            "text",
            "created_at",
            "updated_at",
        )
