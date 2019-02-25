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
    path('<slug:slug>/preview/', PostPreviewView.as_view(), name='post-preview'),
    path('<slug:slug>/', PostDetailView.as_view(), name='post-detail'),
    path('<slug:slug>/comment/', CommentCreateView.as_view(), name='add-comment'),
    path('<slug:slug>/update/', PostUpdateView.as_view(), name='post-update'),
    path('<slug:slug>/delete/', PostDeleteView.as_view(), name='post-delete'),
]