from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import generic
from .models import BlogPost


def home(request):
    latest_blog_posts = BlogPost.objects.order_by('-pub_date')[:10]
    return render(request, 'blogPosts/home.html', {'latest_blog_posts': latest_blog_posts})


def detail(request, post_id):
    post = get_object_or_404(BlogPost, pk=post_id)
    return render(request, 'blogPosts/detail.html', {'post': post})
