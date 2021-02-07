from django.urls import path
from .views import home, contact, like_view, BlogView, AddPostView, UpdatePostView, DeletePostView, \
    blog_detail

urlpatterns = [
    path('', home, name='home'),
    path('contact/', contact, name='contact'),
    path('blog/', BlogView.as_view(), name='blog'),
    path('blog-detail/<int:pk>', blog_detail, name='blog-detail'),
    path('add-post/', AddPostView.as_view(), name='add-post'),
    path('blog-detail/edit/<int:pk>', UpdatePostView.as_view(), name='update-post'),
    path('blog-detail/<int:pk>/remove', DeletePostView.as_view(), name='delete-post'),
    path('like/<int:pk>', like_view, name='like-post'),

]
