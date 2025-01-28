from django.shortcuts import render
from .models import SafariPackage, GalleryImage, HeroImage, Gallery

def home(request):
    # Fetch data from models
    hero_images = HeroImage.objects.all()
    gallery_images = GalleryImage.objects.all()
    safari_packages = SafariPackage.objects.all()

    # Pass the data to the template context
    return render(request, 'home/home.html', {
        'hero_images': hero_images,
        'gallery_images': gallery_images,
        'safari_packages': safari_packages,
    })
    



def gallery(request):
    gallery_instance = Gallery.objects.all()
    return render(request, 'home/gallery.html', {'Gallery': gallery_instance})



def contact(request):
    return render(request, 'home/contact.html')



