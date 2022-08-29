from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.home, name="home"),
    path("signup/", views.signup, name="signup"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("users/", views.users, name="users"),
    path("user/details/<int:user_id>", views.details, name="details"),
    path("password-done/", views.password, name="password"),
    path('change-password/',
         auth_views.PasswordChangeView.as_view(template_name='password.html', success_url='/password-done/'),
         name='change_password'),
    path(
        "reset-password/",
        auth_views.PasswordResetView.as_view(template_name="password_reset_form.html"),
        name="reset_password",
    ),
    path(
        "password-reset-done/",
        auth_views.PasswordResetDoneView.as_view(
            template_name="password_reset_done.html"
        ),
        name="password_reset_done",
    ),
    path(
        "confirm-password/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="password_reset_confirm.html",
        ),
        name="password_reset_confirm",
    ),
    path(
        "password-reset-complete/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="password_reset_complete.html",
        ),
        name="password_reset_complete",
    ),
]
