from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from . import models
from django.db.models import Q

def posts_by_catagory(request , catagory_id):
    posts =models.Blog.objects.filter(catagory=catagory_id,status='PUBLISHED').order_by('-created_at')
    try:
        catagory=models.Catagory.objects.get(id=catagory_id)
    except:
       
        catagory=get_object_or_404(models.Catagory,pk=catagory_id)
    context ={
        
        'posts':posts,
        'catagory':catagory,
    }
    return render(request,'posts_by_catagory.html',context)



def blogs(request,slug):
    single_post=get_object_or_404(models.Blog,slug=slug,status='PUBLISHED')
    if request.method=="POST":
        comment=models.Comment()
        comment.user=request.user
        comment.post=single_post
        comment.comment=request.POST['comment']
        comment.save()
        return redirect('blogs',slug=single_post.slug)
    
    
    
    comments =models.Comment.objects.filter(post=single_post)
    context={'single_post':single_post,'comments':comments}
    return render(request,'blogs.html',context)


def search(request):
    keyword=request.GET.get('keyword')
  
  
    blogs=models.Blog.objects.filter(Q(title__icontains=keyword)|Q(short_describtion__icontains=keyword)|Q(blog_body__icontains=keyword),status='PUBLISHED')
    context={'blogs':blogs}
    return render(request,'search.html',context)