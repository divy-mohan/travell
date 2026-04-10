from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'safari-packages', views.SafariPackageViewSet)
router.register(r'gallery-images', views.GalleryImageViewSet)
router.register(r'hero-images', views.HeroImageViewSet)
router.register(r'gallery', views.GalleryViewSet)
router.register(r'agent', views.DynamicAgentViewSet)

urlpatterns = [
    path('', views.home, name='home'),
    path('gallery/', views.gallery, name='gallery'),
    path('contact/', views.contact, name='contact'),
    path('api/v1/', include(router.urls)),
]

# Add static URL pattern for media files
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
