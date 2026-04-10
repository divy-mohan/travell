import os
import django
import json
import sys

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'neem_karoli_travellers.settings')
django.setup()

from home.models import DynamicTravelAgent

def populate_mock_data():
    print("Clearing existing agent profiles...")
    DynamicTravelAgent.objects.all().delete()
    
    print("Creating 'Home' Default Agent...")
    DynamicTravelAgent.objects.create(
        page_slug='home',
        agent_name='Neem Karoli Guide',
        theme_color='#FF9900',  # Warm Orange for Home
        teaser_messages=['👋 Welcome!', 'Looking for spiritual peace?', 'Hi there!'],
        greeting_messages=['Namaste! Welcome to Neem Karoli Travellers. How can I assist your journey?'],
        suggested_prompts=['View Chardham Yatra', 'Book a Safari', 'Contact Support'],
        is_active=True
    )
    
    print("Creating 'Jim Corbett' Agent...")
    DynamicTravelAgent.objects.create(
        page_slug='jim-corbett',
        agent_name='Ranger Rahul',
        theme_color='#2E8B57',  # Safari Green
        teaser_messages=['🦁 Spot a tiger?', 'Ready for adventure?', 'Explore the jungle!'],
        greeting_messages=['Welcome to the wild! I am Ranger Rahul. Ready to book your thrilling Jim Corbett Safari?'],
        suggested_prompts=['Show Package Details', 'What is the price?', 'Best time to visit?'],
        is_active=True
    )

    print("\n--- Mock Data Successfully Created! ---")
    print(f"Total Agents Created: {DynamicTravelAgent.objects.count()}")

if __name__ == '__main__':
    populate_mock_data()
