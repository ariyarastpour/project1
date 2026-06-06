from django import template
from blog.models import Post,Category
register = template.Library()

#recent-posts
@register.inclusion_tag('blog/blog-recent-posts.html')
def recent_posts():
    recent_posts = Post.objects.filter(status=1).order_by('published_date')[:6]
    return {'recent_posts':recent_posts}

@register.inclusion_tag('blog/blog-footer-recent-posts.html')
def recent_posts_footer():
    recent_posts = Post.objects.filter(status=1).order_by('published_date')[:6]
    return {'recent_posts':recent_posts}

#categories
@register.inclusion_tag('blog/blog-categories.html')
def posts_categories():
    posts = Post.objects.filter(status=1)
    categories = Category.objects.all()
    cat_dict = {}
    for name in categories:
        cat_dict[name]=posts.filter(category=name).count()
    return {'categories':cat_dict}

@register.inclusion_tag('blog/blog-categories-footer.html')
def posts_categories_footer():
    posts = Post.objects.filter(status=1)
    categories = Category.objects.all()
    cat_dict = {}
    for name in categories:
        cat_dict[name]=posts.filter(category=name).count()
    return {'categories':cat_dict}

@register.inclusion_tag('blog/blog-categories-nav.html')
def posts_categories_header():
    posts = Post.objects.filter(status=1)
    categories = Category.objects.all()
    cat_dict = {}
    for name in categories:
        cat_dict[name]=posts.filter(category=name).count()
    return {'categories':cat_dict}