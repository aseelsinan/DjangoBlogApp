
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from . import views
urlpatterns = [
    path('<int:catagory_id>/',views.posts_by_catagory,name='posts_by_catagory'),
    

]