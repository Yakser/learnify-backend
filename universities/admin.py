from django.contrib import admin

from universities.models import University, Department, Specialization


class SpecializationInline(admin.TabularInline):
    model = Specialization


class DepartmentInline(admin.TabularInline):
    model = Department


@admin.register(Specialization)
class SpecializationAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "get_department_name",
        "get_department_university",
    )
    list_display_links = (
        "id",
        "name",
    )

    def get_department_name(self, obj):
        return obj.department.name

    def get_department_university(self, obj):
        return obj.department.university.name


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    inlines = [SpecializationInline]

    list_display = (
        "id",
        "name",
        "get_university_name",
    )
    list_display_links = (
        "id",
        "name",
    )

    def get_university_name(self, obj):
        return obj.university.name


@admin.register(University)
class UniversityAdmin(admin.ModelAdmin):
    inlines = [DepartmentInline]

    list_display = (
        "id",
        "name",
    )
    list_display_links = (
        "id",
        "name",
    )
