from django.shortcuts import render, get_object_or_404
from .models import Workout

#lIST OF VIEW - SHOW ALL WORKOUTS 
def workout_list(request):
    workouts = Workout.objects.all().order_by('-date')
    return render(request, 'workouts/workout_list.html', {'workouts': workouts})

#DETAIL VIEW SHOW ONE WORKOUT BY ID 

def workout_detail(request, pk):
    workout = get_object_or_404(Workout, pk=pk)
    return render(request, 'workouts/workout_detail.html', {'workout': workout})
