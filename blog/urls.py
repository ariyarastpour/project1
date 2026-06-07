from django.urls import path
from blog.views import *
app_name = 'blog'

urlpatterns = [
    path('', blog_view, name='index'),
    path('/<int:pid>',blog_pid, name='pid'),
    #author url
    path('/author/<str:author_username>',blog_view ,name='author' ),
    #categories url
    path('/category/<str:cat_name>',blog_view,name='category'),
    #search url
    path('/search/',blog_search ,name='search')
]