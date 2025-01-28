# Create your views here.
from django.shortcuts import render
from .models import Package

# Create your views here.
def packages(request):
    safari_packages = Package.objects.all()  # Get all packages from the database
    return render(request, 'packages/packages.html', {'safari_packages': safari_packages})

# Create your views here.
def Jim_Corbett_National_Park(request):
    return render(request, 'packages/Jim_Corbett_National_Park.html')
# Create your views here.
def neem_karoli(request):
    return render(request, 'packages/neem_karoli.html')
# Create your views here.
def chardham_yatra(request):
    return render(request, 'packages/chardham_yatra.html')
# Create your views here.
def adventure(request):
    return render(request, 'packages/adventure.html')