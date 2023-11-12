from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from core.permissions import IsStaffOrReadOnly
from news.models import News
from news.pagination import NewsPagination
from news.serializers import NewsListSerializer


class NewsViewSet(viewsets.ModelViewSet):
    serializer_class = NewsListSerializer
    permission_classes = [IsAuthenticated]
    queryset = News.objects.all()
    pagination_class = NewsPagination
    CACHE_KEY_PREFIX = "news-viewset"

    def get_permissions(self):
        if self.action == "create":
            permission_classes = [IsAuthenticated]
        elif self.action in ["update", "partial_update", "delete"]:
            permission_classes = [IsStaffOrReadOnly]
        else:
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @action(detail=True, methods=["get"])
    def generate_short_text(self, request, pk=None):
        news_post = self.get_object()
        news_post.short_text = news_post.text[:50] + "..."
        news_post.save()
        return Response({"detail": "short_text have been generated"})

    def destroy(self, request, *args, **kwargs):
        response = super().destroy(request, *args, **kwargs)
        return response

    def partial_update(self, request, *args, **kwargs):
        response = super().partial_update(request, *args, **kwargs)
        return response

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        return response
