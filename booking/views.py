from django.shortcuts import render, redirect
from .forms import BookingForm, HotelBookingForm
from .models import CarouselImage

# Create your views here.
def safari_booking(request):
    return render(request, 'booking/safari_booking.html')

def booking_view(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('booking_success')
    else:
        form = BookingForm()
    return render(request, 'booking/booking_form.html', {'form': form})



def booking_success(request):
    return render(request, 'booking/booking_success.html')


def book_hotel(request):
    # Fetch all carousel images from the database
    carousel_images = CarouselImage.objects.all()

    if request.method == 'POST':
        form = HotelBookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('booking_success')  # Replace with your success URL
    else:
        form = HotelBookingForm()

    # Pass the form and carousel images to the template
    return render(request, 'booking/hotel_booking.html', {
        'form': form,
        'carousel_images': carousel_images
    })
