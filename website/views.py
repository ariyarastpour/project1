from django.shortcuts import render
from django.http import HttpResponse

def Home_view(request):
    return HttpResponse('<h2>WELL COME TO HOME PAGE</h2>')

def About_view(request):
    return HttpResponse('<h2>WELL COME TO ABOUT PAGE</h2>')

def Contact_view(request):
    return HttpResponse('<h2>WELL COME TO CONTACT PAGE</h2>')
