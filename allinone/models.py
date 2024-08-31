from django.db import models

# Create your models here.

class app(models.Model):
    SUB_CATEGORY_CHOICES = [
        ('featured', 'Featured'),
        ('newly_added', 'Newly Added'),
        ('adult', 'Adult'),
        ('entertainment', 'Entertainment'),
        ('social', 'Social'),
        ('productive', 'Productive'),
        ('communication', 'Communication'),
        ('premium', 'Premium Apps'),
        ('tools_and_utilities ', 'Tools & utilities '),
        ('editor_choice_apps', 'Editor\'s choice Apps'),
        ('editing_apps', 'Editing Apps'),

    ]
    name = models.CharField(max_length=100)
    description = models.TextField()
    rating = models.FloatField()
    video = models.FileField(upload_to='videos/')
    image = models.ImageField(upload_to='images/')
    category = models.CharField(max_length=100)
    sub_category = models.CharField(
        max_length=50,  # Ensure the max_length can accommodate the longest choice value
        choices=SUB_CATEGORY_CHOICES,  # Assign the choices to this field
        default='newly_added'  # Optional: set a default value
    )
    download_link = models.URLField()
    rating_no = models.IntegerField(default=0)
    download_no = models.IntegerField(default=0)
    def __str__(self):
        return self.name
    
class comments(models.Model):
    app = models.ForeignKey(app, on_delete=models.CASCADE)
    rating = models.FloatField()
    comment = models.TextField()

    def __str__(self):
        return self.comment