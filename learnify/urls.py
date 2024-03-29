from django.contrib import admin
from django.urls import include, path, re_path
from rest_framework import permissions
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

schema_view = get_schema_view(
    openapi.Info(
        title="learnify API",
        default_version="v1",
        description="API for learnify project",
    ),
    public=True,
    permission_classes=[permissions.IsAdminUser],
)

urlpatterns = [
    path("__debug__/", include("debug_toolbar.urls")),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    re_path(
        r"^swagger(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    re_path(
        r"^swagger/$",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    re_path(
        r"^redoc/$", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"
    ),
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("auth/", include(("users.urls", "users"), namespace="users")),
    path(
        "universities/",
        include(("universities.urls", "universities"), namespace="universities"),
    ),
    path(
        "news/",
        include(("news.urls", "news"), namespace="news"),
    ),
]
