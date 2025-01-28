from django.db import models

class SafariPackage(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    duration = models.CharField(max_length=50)  # e.g., "3 Days"
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)  # Price of the package
    image = models.ImageField(upload_to='media/packages/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    details_url = models.CharField(max_length=500, blank=True)


    def __str__(self):
        return self.title


class GalleryImage(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to='media/gallery/')
    alt_text = models.CharField(max_length=200, blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title if self.title else f"Image {self.id}"

class HeroImage(models.Model):
    image = models.ImageField(upload_to='media/hero/')
    alt_text = models.CharField(max_length=200)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.alt_text


class Gallery(models.Model):
    title = models.CharField(max_length=255, help_text="Enter a short title for the image")
    image = models.ImageField(upload_to='gallery/', help_text="Upload the image file")
    description = models.TextField(blank=True, help_text="Optional: Add a description for the image")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Gallery"  # Singular name
        verbose_name_plural = "GalleryPG"  # Correct plural name