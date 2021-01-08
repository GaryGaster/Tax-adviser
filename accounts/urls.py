from django.urls import path
from .views import UserRegisterView, UserEditView, PasswordsChangeView, password_success

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('edit-profile/', UserEditView.as_view(), name='edit-profile'),
    path('password/', PasswordsChangeView.as_view(), name='change-password'),
    path('password-success/', password_success, name='password-success')

]
