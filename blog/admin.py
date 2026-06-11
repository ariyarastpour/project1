from django.contrib import admin
from blog.models import Post, Category,Comment

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    search_fields = ['title', 'disc']
    list_display = ('title','status','counted_view', 'created_date','published_date')
    list_filter = ('status','author','category')

class CommentAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    search_fields = ['name', 'message']
    list_display = ('name','approved','post','created_date','updated_date')
    list_filter = ('name' ,'post')

admin.site.register(Post ,PostAdmin)
admin.site.register(Comment ,CommentAdmin)
admin.site.register(Category)
