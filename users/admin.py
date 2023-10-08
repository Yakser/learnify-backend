from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from users.models import Profile

User = get_user_model()


class ProfileInlined(admin.StackedInline):
    model = Profile
    can_delete = False


class UserAdmin(UserAdmin, ImportExportModelAdmin):
    inlines = (ProfileInlined,)
    list_display = (
        "username",
        "email",
        "full_name",
        "is_staff",
    )
    list_display_links = (
        "username",
        "email",
        "full_name",
    )
    readonly_fields = ("date_joined",)
    date_hierarchy = "date_joined"
    search_fields = ("username", "first_name", "last_name", "email")

    @admin.display(empty_value="???", description="Полное имя")
    def full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"


admin.site.unregister(User)
admin.site.register(User, UserAdmin)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
    )
    list_display_links = (
        "id",
        "user",
    )

    search_fields = (
        "id",
        "user",
    )


class UsersResource(resources.ModelResource):
    class Meta:
        model = User
