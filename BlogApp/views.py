from django.shortcuts import  redirect, render
from Blogs import models
from .froms import RegiserationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
def home(request):
    featured_post=models.Blog.objects.filter(is_featured=True,status='PUBLISHED').order_by('-updated_at')
    posts=models.Blog.objects.filter(is_featured=False,status='PUBLISHED').order_by('-updated_at')
    
    
       
    context = {
        "featured_post":featured_post,
        'posts':posts,
        
    }
    return render(request, "home.html", context)

def register(request):
    if request.method == 'POST':
        form=RegiserationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    else:
        form=RegiserationForm()
    context={'form':form}
    return render(request,'register.html',context)
    



def login(request):
    if request.method=='POST':
        form = AuthenticationForm(request,request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=auth.authenticate(username=username,password=password)
            if user is not None:
                auth.login(request,user)    
            return redirect('dashboard')
    
    form = AuthenticationForm()
    context={
        "form":form
    }
    return render(request,'login.html',context)



def logout(request):
    auth.logout(request)
    return redirect('home')