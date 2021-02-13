from django.shortcuts import render
from blog.models import Blog

# Create your views here.

def home (request):
    return render(request,'webpages/home.html')

def about (request):
    return render(request,'webpages/about.html')

def blog (request):
    all_blogs = Blog.objects.all()
    data = {
        'all_blogs': all_blogs,
    }
    return render(request,'webpages/blog.html',data)



