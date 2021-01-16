from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect


from .models import Post, Comment
from .forms import PostForm, EditPostForm, CommentForm


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


def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('blog-detail', args=[str(pk)]))


class BlogView(ListView):
    model = Post
    template_name = 'main/blog.html'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'main/blog_single.html'


    def get_context_data(self, *args, **kwargs):
        context = super(BlogDetailView, self).get_context_data(*args, **kwargs)

        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()

        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True

        context['total_likes'] = total_likes
        context['liked'] = liked

        return context


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'main/add_post.html'


class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'main/add_comment.html'

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)


class UpdatePostView(UpdateView):
    model = Post
    form_class = EditPostForm
    template_name = 'main/update_post.html'


class DeletePostView(DeleteView):
    model = Post
    template_name = 'main/delete_post.html'
    success_url = reverse_lazy('blog')
