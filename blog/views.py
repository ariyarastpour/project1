from django.shortcuts import render , get_object_or_404
from blog.models import Post,Category

def blog_view(request):
    posts = Post.objects.filter(status=1)
    categories = Category.objects.filter(post__in=posts).distinct()
    recent_posts = Post.objects.filter(status=1).order_by('-published_date')[:6]
    first_post = posts.first()
    other_posts = posts[1:]
    context = {
        'recent_posts':recent_posts ,
        'posts':posts ,
        'first_post':first_post ,
        'other_posts':other_posts,
        'categories':categories
    }
    return render(request, 'blog/blog-home.html',context)

#Single Page
def blog_pid(request,pid):
    post = get_object_or_404(Post, pk=pid,status=1)
    context = {'post':post}
    return render(request,'blog/blog-single.html',context)

#Page for Categories
def Asia_view(request):
    recent_posts = Post.objects.filter(status=1).order_by('-published_date')[:6]
    posts = Post.objects.filter(status=1, category__name='Asia').distinct().order_by('-published_date')
    first_post = posts.first()
    other_posts = posts[1:]
    context = {
        'recent_posts': recent_posts,
        'posts': posts,
        'first_post': first_post,
        'other_posts': other_posts,
    }
    return render(request, 'blog/Asia_cat.html', context)


def Africa_view(request):
    recent_posts = Post.objects.filter(status=1).order_by('-published_date')[:6]
    posts = Post.objects.filter(status=1)
    first_post = posts.first()
    other_posts = posts[1:]
    context = {
        'recent_posts':recent_posts ,
        'posts':posts ,
        'first_post':first_post ,
        'other_posts':other_posts
    }
    return render(request,'blog/Africa_cat.html',context)

def Europe_view(request):
    posts = Post.objects.filter(status=1)
    recent_posts = Post.objects.filter(status=1).order_by('-published_date')[:6]
    first_post = posts.first()
    other_posts = posts[1:]
    context = {
        'recent_posts':recent_posts ,
        'posts':posts ,
        'first_post':first_post ,
        'other_posts':other_posts
    }
    return render(request,'blog/Europe_cat.html',context)

def North_America_view(request):
    recent_posts = Post.objects.filter(status=1).order_by('-published_date')[:6]
    posts = Post.objects.filter(status=1)
    first_post = posts.first()
    other_posts = posts[1:]
    context = {
        'recent_posts':recent_posts ,
        'posts':posts ,
        'first_post':first_post ,
        'other_posts':other_posts
    }
    return render(request,'blog/North-America.html',context)

def South_America_view(request):
    recent_posts = Post.objects.filter(status=1).order_by('-published_date')[:6]
    posts = Post.objects.filter(status=1)
    first_post = posts.first()
    other_posts = posts[1:]
    context = {
        'recent_posts':recent_posts ,
        'posts':posts ,
        'first_post':first_post ,
        'other_posts':other_posts
    }
    return render(request,'blog/South-America.html',context)