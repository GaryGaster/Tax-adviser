from django.urls import path
from .views import home, contact, BlogView, BlogDetailView

urlpatterns = [
    path('', home, name='home'),
    path('contact/', contact, name='contact'),
    path('blog/', BlogView.as_view(), name='blog'),
    path('blog-detail/<int:pk>', BlogDetailView.as_view(), name='blog-detail'),

]
