import reprlib

from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from import_export.fields import Field
from import_export.widgets import DateWidget

from users.models import Profile

User = get_user_model()


class UsersResource(resources.ModelResource):
    last_login = Field(
        attribute="last_login",
        column_name="last_login",
        widget=DateWidget(format="%d.%m.%Y"),
    )
    fullname = Field()
    about_info = Field()

    def dehydrate_fullname(self, user):
        return f"{user.first_name} {user.last_name}"

    def dehydrate_about_info(self, user):
        return reprlib.repr(user.profile.about).strip("'")

    def get_queryset(self):
        return self._meta.model.objects.filter(is_active=True)

    def dehydrate_email(self, user):
        return f"{user.email[:3]}***{user.email[-3:]}"

    class Meta:
        model = User
        fields = ("id", "fullname", "email", "last_login", "about_info")
        export_order = ("id", "fullname", "email", "last_login", "about_info")
        name = "Export/Import only public users data"


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
    resource_classes = [UsersResource]

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
