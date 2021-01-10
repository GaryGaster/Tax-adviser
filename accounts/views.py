from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import DetailView
from main.models import Profile

from .forms import SignUpForm, EditProfileForm, PasswordChangingForm


class ShowProfilePageView(DetailView):
    model = Profile
    template_name = 'registration/user_profile.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)

        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])

        context['page_user'] = page_user
        return context


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
