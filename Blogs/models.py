from django.db import models
from django.contrib.auth.models import User

class Catagory(models.Model):
    catagory_name=models.CharField(max_length=50,unique=True)
    created_at =models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.catagory_name
    
    class Meta:
        verbose_name_plural='catagories'
    
STATUS_CHOICES=(
    ('DRAFT','DRAFT'),
    ('PUBLISHED','PUBLISHED')
)
class Blog (models.Model):
    title =models.CharField(max_length=100)
    slug=models.SlugField(max_length=150,unique=True,blank=True)
    catagory=models.ForeignKey(Catagory,on_delete=models.CASCADE)
    author=models.ForeignKey(User,  on_delete=models.CASCADE)
    featured_image=models.ImageField(upload_to='uploads/%Y/%m/%d/')
    short_describtion=models.TextField(max_length=500)
    blog_body=models.TextField(max_length=2000)
    status =models.CharField(max_length=15,default='DRAFT',choices=STATUS_CHOICES)
    is_featured=models.BooleanField(default=False)
    created_at =models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    
class About(models.Model):
    about_heading=models.CharField( max_length=25)
    about_description =models.TextField(max_length=255)
    created_at =models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.about_heading
    

    class Meta:
        verbose_name_plural='About'
        
        
        
class SocialMediaLinks(models.Model):
    platform=models.CharField( max_length=26)
    link=models.URLField(max_length=100)
    created_at =models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.platform



class Comment(models.Model):
    user =models.ForeignKey(User ,on_delete=models.CASCADE)
    post =models.ForeignKey(Blog, on_delete=models.CASCADE)
    comment=models.TextField(max_length=250)
    created_at =models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment