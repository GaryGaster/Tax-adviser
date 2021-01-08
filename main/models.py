from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField


class Post(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField(blank=True, null=True)
    post_date = models.DateField(auto_now_add=True)
    snippet = models.CharField(max_length=255, default="")
    likes = models.ManyToManyField(User, related_name='blog_posts')

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def post_date_pretty(self):
        return self.post_date.strftime("%Y-%m-%d")

    def get_absolute_url(self):
        return reverse('blog-detail', args=[str(self.id)])
