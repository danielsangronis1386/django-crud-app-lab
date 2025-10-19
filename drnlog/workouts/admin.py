from django.contrib import admin
from . models import Workout, Exercise

@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'duration')
    search_fields = ('name',)

@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'workout', 'sets', 'reps', 'weight')
    list_filter = ('category', 'workout')
    search_fields = ('name',)

