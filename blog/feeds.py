from django.contrib.syndication.views import Feed
from .models import Post


class RssTutorialsFeeds(Feed):
    title = "blog posts"
    link = "/rss-feeds"
    description = "These posts are the best posts!"

    def items(self):
        return Post.objects.filter(status=1)

    def item_title(self, item):
        return item.title

    def item_discription(self, item):
        return item.disc