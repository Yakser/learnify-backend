from django.urls import path

from universities.views import (
    UniversityList,
    UniversityDetail,
    SpecializationList,
    DepartmentList,
    # UniversityDepartmentList,
    # UniversityDepartmentDetail,
    SpecializationDetail,
    DepartmentDetail,
)

app_name = "universities"

urlpatterns = [
    path("", UniversityList.as_view()),
    path("<int:pk>/", UniversityDetail.as_view()),
    path("departments/", DepartmentList.as_view()),
    path(
        "departments/<int:pk>/",
        DepartmentDetail.as_view(),
    ),
    path("departments/", DepartmentList.as_view()),
    path("specializations/", SpecializationList.as_view()),
    path("specializations/<int:pk>/", SpecializationDetail.as_view()),
]
