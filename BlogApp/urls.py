from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings
from Blogs import views as BlogsView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('blogs/<slug:slug>/', BlogsView.blogs, name='blogs'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('blogs/search/', BlogsView.search, name='search'),

    # Blogs
    path('category/', include('Blogs.urls')),

    # Dashboard
    path('dashboard/', include('Dashboards.urls'),name='dashboard'),  
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)