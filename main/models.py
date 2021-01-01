from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date


class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    post_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def post_date_pretty(self):
        return self.post_date.strftime("%Y-%m-%d")

    def get_absolute_url(self):
        return reverse('blog-detail', args=[str(self.id)])
