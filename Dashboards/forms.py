from django import forms
from Blogs.models import Catagory ,Blog
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CategoryForm(forms.ModelForm):
    class Meta:
        model=Catagory
        fields='__all__'

class PostsForm(forms.ModelForm):
    class Meta:
        model=Blog
        fields=('title','catagory','featured_image','short_describtion','blog_body','status','is_featured')
        
        
class UsersForm(UserCreationForm):
     class Meta:
        model=User
        fields=('email','username','password1','password2','is_active','is_staff','is_superuser','groups','user_permissions')


