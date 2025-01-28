from django.contrib import admin
from .models import Booking, HotelBooking, CarouselImage

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'preferred_date', 'email', 'phone_number', 'preferred_shift')
    search_fields = ('full_name', 'email', 'phone_number')
    list_filter = ('preferred_date', 'preferred_shift')


@admin.register(HotelBooking)
class HotelBookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'check_in_date', 'check_out_date', 'guests', 'email')
    search_fields = ('name', 'email', 'phone')
    

admin.site.register(CarouselImage)
