from django.db import models

# Create your models here.
class Recipe(models.Model):
    recipe_name = models.CharField(max_length =25, default='No name provided')
    recipe_desc= models.TextField(default='No description provided')
    recipe_image = models.ImageField(upload_to="recipe")
         