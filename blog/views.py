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
#Single Page
def blog_pid(request,pid):
    post = get_object_or_404(Post, pk=pid,status=1)
    context = {'post':post}
    return render(request,'blog/blog-single.html',context)
#Page for Categories
def Asia_view(request):
    posts = Post.objects.filter(status=1)
    context = {'post':posts}
    return render(request,'blog/Asia_cat.html',context)

def Africa_view(request):
    posts = Post.objects.filter(status=1)
    context = {'posts':posts}
    return render(request,'blog/Africa_cat.html',context)

def Europe_view(request):
    post = Post.objects.filter(status=1)
    context = {'post':post}
    return render(request,'blog/Europe_cat.html',context)

def North_America_view(request):
    post = Post.objects.filter(status=1)
    context = {'post':post}
    return render(request,'blog/North-America_cat.html',context)

def South_America_view(request):
    post = Post.objects.filter(status=1)
    context = {'post':post}
    return render(request,'blog/South-America.html',context)