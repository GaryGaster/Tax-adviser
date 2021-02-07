from django.contrib import admin
from .models import Post, Profile, Comment

admin.site.register((Post, Profile))


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'body', 'post', 'timestamp')
    list_filter = ('timestamp',)
