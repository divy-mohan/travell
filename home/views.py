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





from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import SafariPackageSerializer, GalleryImageSerializer, HeroImageSerializer, GallerySerializer, DynamicTravelAgentSerializer
from .models import SafariPackage, GalleryImage, HeroImage, Gallery, DynamicTravelAgent

class SafariPackageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SafariPackage.objects.all()
    serializer_class = SafariPackageSerializer

class GalleryImageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = GalleryImage.objects.all()
    serializer_class = GalleryImageSerializer

class HeroImageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = HeroImage.objects.all()
    serializer_class = HeroImageSerializer

class GalleryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer

class DynamicAgentViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = DynamicTravelAgent.objects.all()
    serializer_class = DynamicTravelAgentSerializer
    lookup_field = 'page_slug'
    
    def list(self, request, *args, **kwargs):
        page_slug = request.query_params.get('page', 'home')
        try:
            agent = DynamicTravelAgent.objects.get(page_slug=page_slug, is_active=True)
            serializer = self.get_serializer(agent)
            return Response(serializer.data)
        except DynamicTravelAgent.DoesNotExist:
            try:
                default_agent = DynamicTravelAgent.objects.get(page_slug='home', is_active=True)
                serializer = self.get_serializer(default_agent)
                return Response(serializer.data)
            except DynamicTravelAgent.DoesNotExist:
                return Response({"detail": "No agent configured."}, status=404)
