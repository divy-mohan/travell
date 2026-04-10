from rest_framework import serializers
from .models import SafariPackage, GalleryImage, HeroImage, Gallery, DynamicTravelAgent

class SafariPackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SafariPackage
        fields = '__all__'

class GalleryImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryImage
        fields = '__all__'

class HeroImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeroImage
        fields = '__all__'

class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = '__all__'

class DynamicTravelAgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = DynamicTravelAgent
        fields = '__all__'

