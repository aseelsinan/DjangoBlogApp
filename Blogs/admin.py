from django.contrib import admin
from . import models

class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('title',)}
    list_display=('title','catagory','author','status','is_featured')
    search_fields=('id','title','catagory__catagory_name','status')
    list_editable=('is_featured','status')
admin.site.register(models.Catagory)
admin.site.register(models.Blog,BlogAdmin)



class AboutAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        count = models.About.objects.all().count()
        if count==0:
            return True
        else: 
            return False

admin.site.register(models.About,AboutAdmin)



admin.site.register(models.SocialMediaLinks)


admin.site.register(models.Comment)