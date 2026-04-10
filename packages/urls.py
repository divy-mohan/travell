from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', views.PackageViewSet)

urlpatterns = [
    path('', views.packages, name='packages'),  # Maps to /packages/
    path('Jim_Corbett_National_Park/', views.Jim_Corbett_National_Park, name='Jim_Corbett_National_Park'),
    path('neem_karoli/', views.neem_karoli, name='neem_karoli'),
    path('chardham_yatra/', views.chardham_yatra, name='chardham_yatra'),
    path('adventure/', views.adventure, name='adventure'),
    path('api/v1/', include(router.urls)),
]
