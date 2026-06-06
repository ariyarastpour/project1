from django.shortcuts import render , get_object_or_404
from blog.models import Post

def blog_view(request,cat_name=None):
    posts = Post.objects.filter(status=1)
    if cat_name:
        posts = posts.filter(category__name=cat_name)
    first_post = posts[0]
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