from django.shortcuts import render,get_object_or_404
from .models import blog

def allblogs(request):
    blogs = blog.objects
    return render(request,'blog/blog.html',{'blogs':blogs})

def detail(request ,blog_id):
    blogdetails = get_object_or_404(blog, pk=blog_id)
    return render(request,'blog/detail.html',{'blog':blogdetails})