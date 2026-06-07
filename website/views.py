from django.shortcuts import render
from blog.views import Post
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage


def Home_view(request):
    posts = Post.objects.filter(status=1)
    first_post = posts.first()
    other_posts = posts[1:]
    posts = Paginator(posts,5)

    #paginations
    try:
       page_number = request.GET.get('page')
       posts = posts.get_page(page_number)
    except PageNotAnInteger:
        posts = posts.get_page(1)
    except EmptyPage:
        posts = posts.get_page(1)
    first_post = posts[0]
    other_posts = posts[1:]

    context = {
        'posts': posts,
        'first_post': first_post,
        'other_posts': other_posts
    }
    return render(request, 'website/index.html', context)

def Base_view(request):
    posts = Post.objects.filter(status=1)
    recent_posts = Post.objects.filter(status=1).order_by('published_date')
    context = {
        'posts':posts,
        'recent_posts':recent_posts
    }
    return render(request, 'website/base.html',context)

def About_view(request):
    return render(request, 'website/about.html')

def Contact_view(request):
    return render(request, 'website/contact.html')
