from django.db import models
from django.urls import reverse

class Workout(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
    duration = models.PositiveIntegerField(help_text="Duration in minutes")
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('workout_detail', kwargs={'pk': self.id})