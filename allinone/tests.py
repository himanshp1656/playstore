from django.test import TestCase

# Create your tests here.
from allinone.models import app
import random
sub_categories = ['featured', 'newly_added', 'adult']
for i in range(10):
    App = app(
        name=f"App {i+1}",
        description=f"This is the description for App {i+1}.",
        rating=random.uniform(1.0, 5.0),  
        video='videos/dummy_video.webm',  
        image='images/dummy_image.png', 
        category='game', 
        sub_category=random.choice(sub_categories)
    )
    App.save()