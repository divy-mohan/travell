from django.urls import path
from booking import views

urlpatterns = [
    path('', views.booking_view, name='booking'),
    path('booking_success/', views.booking_success, name='booking_success'),
    path('book_hotel/', views.book_hotel, name='book_hotel'),
]
