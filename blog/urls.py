from django.urls import path
from blog.views import blog_view ,blog_single ,blog_pid

app_name = 'blog'

urlpatterns = [
    path('', blog_view, name='index'),
    path('/single', blog_single, name='single'),
    path('/<int:pid>',blog_pid, name='pid')
]