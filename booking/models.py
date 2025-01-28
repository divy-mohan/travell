# booking/models.py

from django.db import models

# Model for defining package options
class PackageOption(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Main Booking model
class Booking(models.Model):
    # Basic Details
    full_name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)

    # Contact Information
    email = models.EmailField()
    phone_number = models.IntegerField()
# Government ID Information
    GOVT_ID_CHOICES = [
        ('Aadhaar Card', 'Aadhaar Card'),
        ('PAN Card', 'PAN Card'),
        ('Passport', 'Passport'),
        ('Voter ID', 'Voter ID'),
        ('Driving License', 'Driving License'),
        ('Other', 'Other'),
    ]
    govt_id_type = models.CharField(
        max_length=50,
        choices=GOVT_ID_CHOICES,
        default='Aadhaar Card',
        verbose_name="Government ID Type"
    )
    govt_id_other = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name="Specify Other ID Type"
    )
    govt_id_number = models.CharField(
        max_length=50,
        verbose_name="Government ID Number",
        default="---------"
    )

    # Safari Preferences
    preferred_date = models.DateField()
    preferred_shift = models.CharField(max_length=50)
    alternative_dates = models.TextField(
        help_text="List alternative dates separated by commas."
    )

    # Package Preferences
    PACKAGE_CHOICES = [
        ('Jim Corbett Jungle Safari', 'Jim Corbett Jungle Safari'),
        ('Neem Karoli Mandir', 'Neem Karoli Mandir'),
        ('Chardham Yatra', 'Chardham Yatra'),
        ('Adventure Package', 'Adventure Package'),
    ]
    selected_package = models.CharField(
        max_length=50,
        choices=PACKAGE_CHOICES,
        # default='Jim Corbett Jungle Safari',
        help_text="Select a single package from the options.",
    )
    # Group Information
    number_of_adults = models.PositiveIntegerField(default=0)
    number_of_children = models.PositiveIntegerField(default=0)


    # Additional Preferences
    preferred_duration = models.CharField(max_length=50)
    accommodation_help = models.BooleanField(default=False)
    accommodation_preferences = models.TextField(blank=True, null=True)
    pickup_drop_service = models.BooleanField(default=False)
    special_requests = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.full_name} - {self.preferred_date}"




class HotelBooking(models.Model):
    GUEST_COUNT_CHOICES = [(i, str(i)) for i in range(1, 11)]  # Guest count (1-10)

    name = models.CharField(max_length=200)  # Guest's full name
    email = models.EmailField()  # Guest's email
    phone = models.CharField(max_length=15)  # Phone number
    check_in_date = models.DateField()  # Check-in date
    check_out_date = models.DateField()  # Check-out date
    guests = models.IntegerField(choices=GUEST_COUNT_CHOICES)  # Number of guests
    special_requests = models.TextField(blank=True, null=True)  # Optional requests

    def __str__(self):
        return f"Booking by {self.name} ({self.check_in_date} - {self.check_out_date})"


class CarouselImage(models.Model):
    image = models.ImageField(upload_to='carousel_images/')
    alt_text = models.CharField(max_length=255)

    def __str__(self):
        return self.alt_text