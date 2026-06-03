from django.shortcuts import render
from blog.views import Post

def Home_view(request):
    posts = Post.objects.filter(status=1)
    first_post = posts.first()
    other_posts = posts[1:]
    recent_posts = Post.objects.filter(status=1).order_by('-published_date')

    context = {
        'recent_posts': recent_posts,
        'posts': posts,
        'first_post': first_post,
        'other_posts': other_posts
    }
    return render(request, 'website/index.html', context)

def About_view(request):
    return render(request, 'website/about.html')

def Contact_view(request):
    return render(request, 'website/contact.html')
