from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User,on_delete=models.SET_NULL,null =True)
    title = models.CharField(max_length=155)
    disc = models.TextField()
    #image
    #category
    counted_view = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    created_date = models.DateField(auto_now_add=True)
    updated_date = models. DateField(auto_now=True)
    published_date = models.DateField(null=True)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.title