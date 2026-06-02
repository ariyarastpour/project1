from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=155)
    disc = models.TextField()
    #image
    #category
    #author
    counted_view = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    created_date = models.DateField(auto_now_add=True)
    updated_date = models. DateField(auto_now=True)
    published_date = models.DateField(null=True)

    def __str__(self):
        return self.title