from django.urls import path
from .views import UserRegisterView, UserEditView, PasswordsChangeView, password_success, ShowProfilePageView, \
    EditProfilePageView, CreateProfilePageView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('edit-profile/', UserEditView.as_view(), name='edit-profile'),
    path('password/', PasswordsChangeView.as_view(), name='change-password'),
    path('password-success/', password_success, name='password-success'),
    path('<int:pk>/profile/', ShowProfilePageView.as_view(), name='show-profile-page'),
    path('<int:pk>/edit-profile-page/', EditProfilePageView.as_view(), name='edit-profile-page'),
    path('create-profile-page/', CreateProfilePageView.as_view(), name='create-profile-page'),

]
