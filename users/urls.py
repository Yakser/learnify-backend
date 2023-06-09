from django.urls import path

from users.views import (
    UserDetail,
    UserList,
    CurrentUser,
    UserFeed,
)

app_name = "users"

urlpatterns = [
    path("users/", UserList.as_view()),
    path("users/<int:pk>/", UserDetail.as_view()),
    path("users/<int:pk>/feed/", UserFeed.as_view()),
    path("users/current/", CurrentUser.as_view()),
    # path("users/reset-password/", EmailResetPassword.as_view()),
    # path("logout/", LogoutView.as_view()),
    # re_path(
    #     r"^account-confirm-email/",
    #     VerifyEmail.as_view(),
    #     name="account_email_verification_sent",
    # ),
    # re_path(
    #     r"^account-confirm-email/(?P<key>[-:\w]+)/$",
    #     VerifyEmail.as_view(),
    #     name="account_confirm_email",
    # ),
    # re_path(
    #     r"^password-reset/",
    #     ResetPassword.as_view(),
    #     name="password_reset_sent",
    # ),
    # re_path(
    #     r"^password-reset/(?P<key>[-:\w]+)/$",
    #     ResetPassword.as_view(),
    #     name="password_reset",
    # ),
]
