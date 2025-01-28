from django.contrib import admin
from .models import Gallery, SafariPackage, GalleryImage, HeroImage

@admin.register(SafariPackage)
class SafariPackageAdmin(admin.ModelAdmin):
    list_display = ('title', 'duration', 'price', 'created_at', 'details_url')
    list_editable = ('details_url',)
    search_fields = ('title', 'description')
    list_filter = ('created_at',)


@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'alt_text', 'uploaded_at')
    search_fields = ('title', 'alt_text')


@admin.register(HeroImage)
class HeroImageAdmin(admin.ModelAdmin):
    list_display = ('alt_text', 'uploaded_at')
    search_fields = ('alt_text',)


# Register the Gallery model
@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')  # Fields to display in the admin list view
    search_fields = ('title', 'description')  # Fields for the search bar
    list_filter = ('created_at',)  # Add a filter sidebar for the created_at field
    ordering = ('-created_at',)  # Order the list view by created_at descending
