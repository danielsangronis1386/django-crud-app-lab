from django.shortcuts import render, redirect, get_object_or_404
from .models import Workout

#lIST OF VIEW - SHOW ALL WORKOUTS 
def workout_list(request):
    workouts = Workout.objects.all().order_by('-date')
    return render(request, 'workouts/workout_list.html', {'workouts': workouts})

#DETAIL VIEW SHOW ONE WORKOUT BY ID 

def workout_detail(request, pk):
    workout = get_object_or_404(Workout, pk=pk)
    return render(request, 'workouts/workout_detail.html', {'workout': workout})

def workout_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        duration = request.POST.get('duration')
        notes = request.POST.get('notes')

        Workout.objects.create(name=name, duration=duration, notes=notes)
    
    return render(request, 'workouts/workout_form.html')
