from django.shortcuts import render
from blog.models import Post
from blog.models import Page

def index(request):
  posts = Post.objects.filter(published=True)
  pages = Page.objects.all
  return render(request, 'blog/index.html', {'posts': posts})

def post(request, slug):
  post = get_object_or_404(Post, slug=slug)
  return render(request, 'blog/post.html', {'post': post})
