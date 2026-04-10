from django.urls import path, include
from booking import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'submit', views.BookingViewSet)
router.register(r'hotel', views.HotelBookingViewSet)
router.register(r'carousel', views.CarouselImageViewSet)

urlpatterns = [
    path('', views.booking_view, name='booking'),
    path('booking_success/', views.booking_success, name='booking_success'),
    path('book_hotel/', views.book_hotel, name='book_hotel'),
    path('api/v1/', include(router.urls)),
]
