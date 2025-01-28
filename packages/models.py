from django.db import models

class Package(models.Model):
    title = models.CharField(max_length=200)  # Title of the package
    description = models.TextField()  # Description of the package
    image = models.ImageField(upload_to='images/tour/')  # Package image
    duration = models.CharField(max_length=100, blank=True)  # Duration of the tour
    activities = models.TextField()  # Activities included in the package
    inclusions = models.TextField()  # Inclusions in the package
    exclusions = models.TextField(blank=True)  # Exclusions in the package
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)  # Price of the package

    def __str__(self):
        return self.title
