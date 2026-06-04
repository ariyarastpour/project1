from django.urls import path
from blog.views import blog_view ,blog_pid,North_America_view, South_America_view, Africa_view, Asia_view, Europe_view 
app_name = 'blog'

urlpatterns = [
    path('', blog_view, name='index'),
    path('/<int:pid>',blog_pid, name='pid'),
    path('/category/Asia', Asia_view, name='Asia'),
    path('/category/Africa', Africa_view, name='Africa'),
    path('/category/Europe', Europe_view, name='Europe'),
    path('/category/Northe-America', North_America_view, name='North'),
    path('/category/South-America', South_America_view, name='Southe')
]