from django.urls import path
from blog.views import *
from .feeds import RssTutorialsFeeds
app_name = 'blog'

urlpatterns = [
    path('', blog_view, name='index'),
    path('/<int:pid>',blog_single, name='pid'),
    #author url
    path('/author/<str:author_username>',blog_view ,name='author' ),
    #categories url
    path('/category/<str:cat_name>',blog_view,name='category'),
    #search url
    path('/search/',blog_search ,name='search'),
    #rss feeds
    path("/rss-feeds/", RssTutorialsFeeds())
]