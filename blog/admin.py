from django.contrib import admin
from blog.models import Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    search_fields = ['title', 'disc']
    list_display = ('title','status','counted_view', 'created_date','published_date')
    list_filter = ('status',)

admin.site.register(Post ,PostAdmin)
