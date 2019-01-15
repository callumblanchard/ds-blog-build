from django.urls import path
from . import views

app_name = "blogPosts"
urlpatterns = [
    path('', views.home, name='blog-home'),
    path('<int:post_id>/', views.detail, name='detail')
]