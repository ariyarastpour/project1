from django.urls import path
from website.views import Home_view ,About_view ,Contact_view

app_name = 'website'

urlpatterns = [
    path('', Home_view, name='home'),
    path('about/', About_view, name='about'),
    path('contact/', Contact_view, name='contact')
]