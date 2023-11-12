from rest_framework.routers import DefaultRouter

from news.views import (
    NewsViewSet,
)

app_name = "news"
router = DefaultRouter()
router.register("", NewsViewSet, basename="news")


urlpatterns = [
    # some urls will be here later
] + router.urls
