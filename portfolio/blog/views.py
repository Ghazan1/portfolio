from django.shortcuts import render,get_object_or_404
from .models import blog

def allblogs(request):
    blogs = blog.objects

    return  render(request,'blogs/blogs.html',{'blogs':blogs})

def detail(request,blog_id):
    blogs = blog.objects

    return  render(request,'blogs/detail.html',{'blogs':blogs})
    detailblog = get_object_or_404(blog,pk=blog_id)
    return render(request,'blogs/detail.html',{'blog':detailblog})
