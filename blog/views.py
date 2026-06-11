from django.shortcuts import render , get_object_or_404
from blog.models import Post,Comment
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.contrib import messages
from blog.forms import CommentForm

def blog_view(request,**kwargs):
    posts = Post.objects.filter(status=1)
    if kwargs.get('cat_name'):
        posts = posts.filter(category__name=kwargs['cat_name'])
    if kwargs.get('author_username'):
        posts = posts.filter(author__username= kwargs['author_username'])
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
    return render(request, 'blog/blog-home.html', context)

#Single Page
def blog_single(request,pid):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'Thanks for your comment! We will be in touch with you shortly.')
        else:
            messages.add_message(request,messages.ERROR,'Your comment failed to send')
    posts = Post.objects.filter(status=1)
    post = get_object_or_404(posts, pk=pid,status=1)
    comments = Comment.objects.filter(post=post, approved=True)
    form = CommentForm()
    context = {'post':post, 'comments':comments, 'form':form}
    return render(request,'blog/blog-single.html',context)

def blog_search(request):
    posts = Post.objects.filter(status=1)

    if request.method == 'GET':
        query = request.GET.get('s')
        if query:
            posts = posts.filter(disc__icontains=query,title__icontains=query)

    first_post = posts.first()
    other_posts = posts[1:]

    context = {
        'posts': posts,
        'first_post': first_post,
        'other_posts': other_posts
    }
    return render(request, 'blog/blog-home.html', context)