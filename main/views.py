from django.shortcuts import render
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


from .models import Post
from .forms import PostForm, EditPostForm


def home(request):
    return render(request, 'main/home.html')


def contact(request):
    if request.method == 'POST':
        if request.POST.get('email', False):
            name = request.POST['name']
            email = request.POST['email']
            subject = request.POST['subject']
            number = request.POST['number']
            message = request.POST['message']

            message += '\n\n' + name + '\n' + email + '\n' + number
            subject += 'Imię i nazwisko: ' + name + 'mail: ' + email + 'Telefon: ' + number

            send_mail(
                subject,
                message,
                'pa.ko.doradca@gmail.com',
                ['pa.ko.doradca@gmail.com'],
                fail_silently=False
            )

    return render(request, 'main/contact.html')


class BlogView(ListView):
    model = Post
    template_name = 'main/blog.html'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'main/blog_single.html'


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'main/add_post.html'


class UpdatePostView(UpdateView):
    model = Post
    form_class = EditPostForm
    template_name = 'main/update_post.html'


class DeletePostView(DeleteView):
    model = Post
    template_name = 'main/delete_post.html'
    success_url = reverse_lazy('blog')
