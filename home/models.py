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
    
    # SEO Fields
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True, help_text="Unique URL identifier")
    meta_title = models.CharField(max_length=200, blank=True, null=True, help_text="SEO Title")
    meta_description = models.TextField(blank=True, null=True, help_text="SEO Description")
    focus_keyword = models.CharField(max_length=150, blank=True, null=True, help_text="Primary keyword for SEO")


    def __str__(self):
        return self.title


class GalleryImage(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to='media/gallery/')
    alt_text = models.CharField(max_length=200, blank=True, null=True)
    seo_caption = models.CharField(max_length=250, blank=True, null=True, help_text="SEO rich caption for image")
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


class DynamicTravelAgent(models.Model):
    """Dynamic chatbot agent personalities and messages per page"""
    page_slug = models.SlugField(max_length=100, unique=True, help_text="Unique page identifier (e.g., 'home', 'jim-corbett', 'neem-karoli')")
    agent_name = models.CharField(max_length=150, default="Travel Guide", help_text="Name of the bot for this page (e.g., 'Ranger Rahul')")
    agent_avatar = models.ImageField(upload_to='media/agent_avatars/', blank=True, null=True, help_text="Custom avatar image for the chat widget")
    theme_color = models.CharField(max_length=20, default="#007BFF", help_text="Hex color code for the chat bubbles on this page")
    
    teaser_messages = models.JSONField(default=list, help_text="List of short popup strings (e.g., ['👋 Hi!', 'Need help?'])")
    greeting_messages = models.JSONField(default=list, help_text="Full greeting messages when chatbot opens")
    suggested_prompts = models.JSONField(default=list, help_text="Actionable chat chips for users (e.g., ['Show Pricing', 'Itinerary limits?'])")
    
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Dynamic Travel Agent'
        verbose_name_plural = 'Dynamic Travel Agents'
        ordering = ['page_slug']

    def __str__(self):
        return f"{self.agent_name} ({self.page_slug})"