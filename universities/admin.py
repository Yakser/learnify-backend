from django.contrib import admin

from universities.models import University, Department, Specialization


class SpecializationAdmin(admin.TabularInline):
    model = Specialization
    show_change_link = True


class DepartmentAdmin(admin.TabularInline):
    model = Department
    inlines = [SpecializationAdmin]
    show_change_link = True


@admin.register(University)
class UniversityAdmin(admin.ModelAdmin):
    inlines = [DepartmentAdmin]
    show_change_link = True

    list_display = (
        "id",
        "name",
    )
    list_display_links = (
        "id",
        "name",
    )
