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
    
class MusclePart(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Exercise(models.Model):
    CATEGORY_CHOICES = [
        ('Chest', 'Chest'),
        ('Back', 'Back'), 
        ('Legs','Legs'),
        ('Arms', 'Arms'),
        ('Shoulders', 'Shoulders'),
        ('Core', 'Core')
    ]

    workout = models.ForeignKey(Workout, on_delete=models.CASCADE, related_name='exercises')
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    sets = models.PositiveBigIntegerField(default=3)
    reps = models.PositiveBigIntegerField(default=10)
    weight = models.FloatField(default=0, help_text="Lb")
    notes = models.TextField(blank=True)

#Third Model with Associations

    muscle_parts = models.ManyToManyField(MusclePart, related_name='exercises')


    def __str__(self):
        return f"{self.name} ({self.category})"

