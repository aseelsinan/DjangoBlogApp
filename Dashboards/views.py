from django.shortcuts import get_object_or_404, redirect, render
from Blogs import models
from django.contrib.auth.decorators import login_required
from .forms import CategoryForm,PostsForm,UsersForm
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

@login_required(login_url='login')
def dashboard(request):
    catagories_count=models.Catagory.objects.all().count
    bosts_count=models.Blog.objects.all().count
    context ={"catagories_count":catagories_count,
              "bosts_count":bosts_count}
    return render(request,'Dashboard/dashboard.html',context)


def catagories(request):
    return render(request,'Dashboard/catagories.html')


def addcatagory(request):
    if request.method=='POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard_categories')
    
    else:
        form = CategoryForm()
    context={
        "form":form
    }

    return render(request,'Dashboard/add_catagory.html',context)


def edit_catagory(request ,pk):
    category=get_object_or_404(models.Catagory,pk=pk)
    if request.method=="POST":
        form = CategoryForm(request.POST,instance=category)
        if form.is_valid():
            form.save()
            return redirect("dashboard_categories")

        
    form = CategoryForm(instance=category)
    context ={"form":form,
              "category":category}

    return render(request,"Dashboard/edit_catagory.html",context)    


def delete_catagory(request,pk):
    category =get_object_or_404(models.Catagory,pk=pk)
    category.delete()
    return redirect("dashboard_categories")



def posts(request):
    posts =models.Blog.objects.all()
    context ={"posts":posts}
    return render(request,'Dashboard/posts.html',context)


def add_post(request):
    if request.method=='POST':
        form =PostsForm(request.POST,request.FILES)
        if form.is_valid():
            post=form.save(commit=False)
            post.author=request.user
            post.save()
            title=form.cleaned_data['title']
            post.slug=slugify(title)+'-'+str(post.id)
            post.save()
            return redirect('posts')
        
    form=PostsForm()
    context={'form':form}
    return render (request,'Dashboard/add_post.html',context)



def edit_post(request,pk):
    post=get_object_or_404(models.Blog,pk=pk)
    if request.method == "POST":
        form =PostsForm(request.POST,request.FILES,instance=post)
        if form.is_valid():
            post = form.save()
            title=form.cleaned_data['title']
            post.slug=slugify(title)+'-'+str(post.id)
            post.save()
            return redirect('posts')

    
    # فائدة حتى يمرر قيمة الحقول من الصفحة الاولى للثانية
    form = PostsForm(instance=post)
    # مرر البوست حتى تقدر ترسل الحدث للسيرفر
    context={'form':form ,'post':post}
    return render (request,'Dashboard/edit_post.html',context)
 
 
 
def delete_post(request , pk):
     post =get_object_or_404(models.Blog,pk=pk) 
     post.delete()
     return redirect('posts')
 
 

def users(request):
    users = User.objects.all()
    context={'users':users}
    return render(request,'dashboard/users.html',context)


def add_users(request):
    if request.method=="POST":
        form = UsersForm(request.POST)
        if form.is_valid():
            form.save()
            print('success')
            return redirect("users")
   
    form = UsersForm()
    context={'form':form}
    return render (request,"dashboard/add_users.html",context)


def edit_user(request,pk):
    user = get_object_or_404(User,pk=pk)
    if request.method=="POST":
        form = UsersForm(request.POST,instance=user)
        if form.is_valid():
            form.save()
            return redirect('users')
    form =UsersForm(instance=user)
    context={'form':form,'user':user}
    return render (request,"dashboard/edit_user.html",context)





def delete_user(request,pk):
    user = get_object_or_404(User,pk=pk)
    user.delete()
    return redirect('users')