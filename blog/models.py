from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=155)

    def __str__(self):
        return self.name

class Post(models.Model):
    author = models.ForeignKey(User,on_delete=models.SET_NULL,null =True)
    title = models.CharField(max_length=155)
    disc = models.TextField()
    image = models.ImageField(upload_to='blog_posts',default='blog_posts/home-banner.jpg')
    author_bio = models.CharField(max_length=400,default='Author Biography')
    author_image = models.ImageField(upload_to='blog_posts',default='blog_posts/images.png')
    category = models.ManyToManyField(Category)
    counted_view = models.PositiveIntegerField(default=0)
    status = models.BooleanField(default=False)
    created_date = models.DateField(auto_now_add=True)
    updated_date = models. DateField(auto_now=True)
    published_date = models.DateField(null=True)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('blog:pid',kwargs={'pid':self.id})
    
class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    name = models.CharField(max_length=155)
    email = models.EmailField()
    message = models.TextField()
    approved = models.BooleanField(default=False)
    created_date = models.DateField(auto_now_add=True)
    updated_date = models. DateField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-created_date']