from django.urls import path
from blog.views import *
app_name = 'blog'

urlpatterns = [
    path('', blog_view, name='index'),
    path('/<int:pid>',blog_pid, name='pid'),
    #categories
    path('/category/<str:cat_name>',category_view,name='category')
]