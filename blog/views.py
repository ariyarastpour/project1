from django.shortcuts import render , get_object_or_404
from blog.models import Post

def blog_view(request):
    posts = Post.objects.filter(status=1)
    first_post = posts.first()
    other_posts = posts[1:]
    recent_posts = Post.objects.filter(status=1).order_by('-published_date')[:6]
    context = {
        'recent_posts':recent_posts ,
        'posts':posts ,
        'first_post':first_post ,
        'other_posts':other_posts
    }
    return render(request, 'blog/blog-home.html',context)

def blog_single(request):
    post = Post.objects.filter(status=1)
    context = {'post':post}
    return render(request, 'blog/blog-single.html', context)

def blog_pid(request,pid):
    post = get_object_or_404(Post, pk=pid)
    context = {'post':post}
    return render(request,'blog/blog-single.html',context)