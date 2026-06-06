from django.shortcuts import render , get_object_or_404
from blog.models import Post,Category

def blog_view(request):
    posts = Post.objects.filter(status=1)
    first_post = posts.first()
    other_posts = posts[1:]

    context = {
        'posts': posts,
        'first_post': first_post,
        'other_posts': other_posts
    }
    return render(request, 'blog/blog-home.html', context)

#Single Page
def blog_pid(request,pid):
    posts = Post.objects.filter(status=1)
    post = get_object_or_404(posts, pk=pid,status=1)
    context = {'post':post}
    return render(request,'blog/blog-single.html',context)

#categories
def category_view(request,cat_name):
    posts = Post.objects.filter(status=1)
    posts = posts.filter(category__name=cat_name)
    context = {'posts':posts}
    return render(request,'blog/blog-home.html',context)