from django.shortcuts import render
from django.http import HttpResponse
from . models import BlogPost


def index(request):
    blogposts = BlogPost.objects.all()
    return render(request, 'index.html', {'blogposts': blogposts})
