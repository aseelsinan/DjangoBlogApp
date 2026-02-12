
from django.urls import path
from . import views
urlpatterns = [
   path('',views.dashboard,name='dashboard'),
   
   # Catagories Crud
   path('catagories/',views.catagories,name='dashboard_categories'),
   path('catagories/add/',views.addcatagory,name='add_catagory'),
   path('catagories/edit/<int:pk>/',views.edit_catagory,name='edit_catagory'),
   path('catagories/delete/<int:pk>/',views.delete_catagory,name='delete_catagory'),
   
   # Posts CRUD
   path("posts/",views.posts,name='posts'),
   path("posts/add",views.add_post,name='add_post'),
   path("posts/edit/<int:pk>",views.edit_post,name='edit_post'),
   path("posts/delete/<int:pk>",views.delete_post,name='delete_post'),


   # Users
   path("users/",views.users,name='users'),
   path("users/add",views.add_users,name='add_users'),
   path("users/edit/<int:pk>",views.edit_user,name='edit_user'),
   path("users/delete/<int:pk>",views.delete_user,name='delete_user'),
]