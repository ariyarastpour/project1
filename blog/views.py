from django.shortcuts import render
from blog.models import Post

def blog_view(request):
    posts = Post.objects.filter(status=1)
    recent_posts = Post.objects.filter(status=1).order_by('-published_date')[:6]
    context = {
        'recent_posts':recent_posts ,
        'posts':posts
    }
    return render(request, 'blog/blog-home.html',context)

def blog_single(request):
    return render(request, 'blog/blog-single.html')