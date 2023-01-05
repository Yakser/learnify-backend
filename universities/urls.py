from django.urls import path

from universities.views import UniversityList, UniversityDetail

app_name = "universities"

urlpatterns = [
    path("", UniversityList.as_view()),
    path("<int:pk>/", UniversityDetail.as_view()),
]
