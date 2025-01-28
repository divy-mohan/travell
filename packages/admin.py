from django.contrib import admin
from .models import Package

class PackageAdmin(admin.ModelAdmin):
    list_display = ('title', 'duration', 'price',)  # What is shown in the list view
    search_fields = ('title',)  # Search by title
    list_filter = ('duration',)  # Filter by duration

admin.site.register(Package, PackageAdmin)
