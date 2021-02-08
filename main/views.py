from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .forms import PostForm, EditPostForm, CommentForm
from .models import Post, Comment


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


def like_view(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return HttpResponseRedirect(reverse('blog-detail', args=[str(pk)]))


def blog_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = Comment.objects.all()
    total_likes = post.total_likes()

    if request.method == 'POST':
        comment_form = CommentForm(request.POST or None)
        if comment_form.is_valid():
            body = request.POST.get('body')
            comment = Comment.objects.create(post=post, user=request.user, body=body)
            comment.save()
            return HttpResponseRedirect(post.get_absolute_url())
    else:
        comment_form = CommentForm()

    context = {
        'post': post,
        'comments': comments,
        'comment_form': comment_form,
        'total_likes': total_likes
    }

    return render(request, 'main/blog_single.html', context)


class BlogView(ListView):
    model = Post
    template_name = 'main/blog.html'
    ordering = ['-id']
    paginate_by = 5


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
