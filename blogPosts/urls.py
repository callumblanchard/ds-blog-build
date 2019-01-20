from django.urls import path
from . import views
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
)

app_name = "blogPosts"
urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('new/', PostCreateView.as_view(), name='post-create'),
    path('<int:post_id>/', PostDetailView.as_view(), name='post-detail'),
    path('<int:post_id>/update/', PostUpdateView.as_view(), name='post-update'),
    path('<int:post_id>/delete/', PostDeleteView.as_view(), name='post-delete'),
]