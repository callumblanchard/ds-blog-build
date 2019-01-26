from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import BlogPost, Comment
from .forms import CommentForm


class PostListView(ListView):
    model = BlogPost
    template_name = 'blogPosts/home.html'
    context_object_name = 'latest_blog_posts'
    ordering = ['-pub_date']

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        context['title'] = "Home"
        return context


class PostDetailView(DetailView):
    model = BlogPost
    template_name = 'blogPosts/detail.html'
    context_object_name = 'post'
    pk_url_kwarg = 'post_id'

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        post = self.get_object()
        context['title'] = post.post_title
        return context


class PostCreateView(LoginRequiredMixin, CreateView):
    model = BlogPost
    fields = [
        'post_title',
        'subtitle',
        'body',
    ]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = BlogPost
    context_object_name = 'post'
    pk_url_kwarg = 'post_id'
    fields = [
        'post_title',
        'subtitle',
        'body',
    ]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = BlogPost
    context_object_name = 'post'
    pk_url_kwarg = 'post_id'

    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


# def add_comment(request, pk):
#     post = get_object_or_404(BlogPost, pk=pk)
#     if request.method == "POST":
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.post = post
#             comment.save()
#             return redirect('post_detail', pk=post.pk)
#     else:
#         form = CommentForm()
#     return render(request, 'comment_form.html', {'form': form})


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    fields = [
        'text',
    ]

    def form_valid(self, form):
        form.instance.username = self.request.user
        form.instance.post = ""# HOW DO WE GET THE BlogPost Model in here?
        return super().form_valid(form)
