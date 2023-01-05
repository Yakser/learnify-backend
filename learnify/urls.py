from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("auth/", include(("users.urls", "users"), namespace="users")),
    path(
        "universities/",
        include(("universities.urls", "universities"), namespace="universities"),
    ),
]