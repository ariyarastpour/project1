from django.urls import path
from website.views import Home_view, About_view, Contact_view
from django.contrib.sitemaps.views import sitemap
from website.sitemaps import StaticViewSitemap
from blog.sitemaps import BlogSitemap

app_name = 'website'

sitemaps = {
    'static': StaticViewSitemap,
    'blog': BlogSitemap
}

urlpatterns = [
    path('', Home_view, name='home'),
    path('about/', About_view, name='about'),
    path('contact/', Contact_view, name='contact'),
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps, "template_name": "sitemap.xml"}, name="sitemap")
]