from django.shortcuts import get_object_or_404, render
from .models import Blog

# Create your views here.

def blog(request):
    blogs = Blog.objects.order_by('-created_date')
    data = {
        'blogs':blogs
    }
    return render(request, 'blog/blog.html', data)

def blog_detail(request, id):
    blog = get_object_or_404(Blog, pk=id)
    data = {
        'blog': blog
    }
    return render(request, 'blog/blog_details.html', data)

def search(request, id):
    return render(request,'blog/search.html',data)
