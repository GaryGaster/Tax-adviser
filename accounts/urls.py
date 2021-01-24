from django.urls import path
from django.contrib.auth import views as auth_views

from .views import UserRegisterView, UserEditView, PasswordsChangeView, password_success, ShowProfilePageView, \
    EditProfilePageView, CreateProfilePageView, PasswordsResetView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('edit-profile/', UserEditView.as_view(), name='edit-profile'),
    path('password/', PasswordsChangeView.as_view(), name='change-password'),
    path('password-success/', password_success, name='password-success'),
    path('<int:pk>/profile/', ShowProfilePageView.as_view(), name='show-profile-page'),
    path('<int:pk>/edit-profile-page/', EditProfilePageView.as_view(), name='edit-profile-page'),
    path('create-profile-page/', CreateProfilePageView.as_view(), name='create-profile-page'),
    path('password-reset/',
         PasswordsResetView.as_view(
             template_name='accounts/password_reset.html'), name='password-reset'),
    path('password-reset-sent/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='accounts/password_reset_sent.html'), name='password-reset-sent'),

    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='accounts/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),

    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='accounts/password_reset_complete.html'), name='password_reset_complete'),

]
