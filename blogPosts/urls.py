from django.urls import path
from . import views
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    CommentCreateView,
    PostPreviewView,
)

app_name = "blogPosts"
urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('new/', PostCreateView.as_view(), name='post-create'),
    path('<int:post_id>/preview/', PostPreviewView.as_view(), name='post-preview'),
    path('<int:post_id>/', PostDetailView.as_view(), name='post-detail'),
    path('<int:post_id>/comment/', CommentCreateView.as_view(), name='add-comment'),
    path('<int:post_id>/update/', PostUpdateView.as_view(), name='post-update'),
    path('<int:post_id>/delete/', PostDeleteView.as_view(), name='post-delete'),
]