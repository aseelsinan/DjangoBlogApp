from . import models
def get_catagories(request):
    catagories=models.Catagory.objects.all()
    return dict(catagories=catagories)

def socialMedia(request):
    socialMedia=models.SocialMediaLinks.objects.all()
    return dict(socialMedia=socialMedia)

def aboutUs(request):
    try:
        about=models.About.objects.get()
        
    except:
        about=None
    return dict(about=about)
    