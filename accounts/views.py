from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from .forms import SignUpForm, EditProfileForm, PasswordChangingForm


class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    template_name = 'registration/change_password.html'
    success_url = reverse_lazy('password-success')


def password_success(request):
    return render(request, 'registration/password_success.html')


class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('password-success')


class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('blog')

    def get_object(self, **kwargs):
        return self.request.user
