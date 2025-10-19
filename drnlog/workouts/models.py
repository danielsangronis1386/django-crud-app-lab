from django.db import models
from django.urls import reverse

#Category

class Category(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    

class Workout(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
    duration = models.PositiveIntegerField(help_text="Duration in minutes")
    notes = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="workouts", null=True, blank=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('workout_detail', kwargs={'pk': self.id})