from django.urls import path

from universities.views import (
    UniversityList,
    UniversityDetail,
    SpecializationList,
    DepartmentList,
    UniversityDepartmentList,
    UniversityDepartmentDetail,
    SpecializationDetail,
)

app_name = "universities"

urlpatterns = [
    path("", UniversityList.as_view()),
    path("<int:pk>/", UniversityDetail.as_view()),
    path("<int:pk>/departments/", UniversityDepartmentList.as_view()),
    path(
        "<int:pk>/departments/<int:department_id>/",
        UniversityDepartmentDetail.as_view(),
    ),
    path("departments/", DepartmentList.as_view()),
    path("specializations/", SpecializationList.as_view()),
    path("specializations/<int:pk>/", SpecializationDetail.as_view()),
]
