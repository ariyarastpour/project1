from django.urls import path
from website.views import Home_view ,About_view ,Contact_view

urlpatterns = [
    path('', Home_view),
    path('about/', About_view),
    path('contact/', Contact_view)
]