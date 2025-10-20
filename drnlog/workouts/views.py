from django.shortcuts import render, redirect, get_object_or_404
from .models import Workout
from .models import Workout, Exercise
from django.http import HttpResponse

#HOME VIEW 
def home(request):
    return render(request, 'workouts/home.html')

#lIST OF VIEW - SHOW ALL WORKOUTS 
def workout_list(request):
    workouts = Workout.objects.all().order_by('-date')
    return render(request, 'workouts/workout_list.html', {'workouts': workouts})

#DETAIL VIEW SHOW ONE WORKOUT BY ID 

def workout_detail(request, pk):
    workout = get_object_or_404(Workout, pk=pk)
    return render(request, 'workouts/workout_detail.html', {'workout': workout})

#CREATE VIEW
def workout_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        duration = request.POST.get('duration')
        notes = request.POST.get('notes')

        Workout.objects.create(
            name=name,
            duration=duration,
            notes=notes
        )
        return redirect('workout_list')

    return render(request, 'workouts/workout_form.html')


#UPDATE VIEW
def workout_update(request, pk):
    workout = get_object_or_404(Workout, pk=pk)

    if request.method == 'POST':
        workout.name = request.POST.get('name')
        workout.duration = request.POST.get('duration')
        workout.notes = request.POST.get('notes')
        workout.save()
        return redirect('workout_detail', pk=workout.id)
    
    return render(request, 'workouts/workout_form.html', {'workout': workout})

#DELETE VIEW 

def workout_delete(request, pk):
    workout = get_object_or_404(Workout, pk=pk)

    if request.method == 'POST':
        workout.delete()
        return redirect('workout_list')
    
    return render(request, 'workouts/workout_confirm_delete.html',{'workout': workout})


# EXERCISE CREATE VIEW 

def exercise_create(request, workout_id):
    workout = get_object_or_404(Workout, pk=workout_id)

    if request.method == 'POST':
        name = request.POST.get('name')
        category = request.POST.get('category')
        sets = request.POST.get('sets')
        reps = request.POST.get('reps')
        weight = request.POST.get('weight')

        Exercise.objects.create(
            workout=workout,
            name=name,
            category=category,
            sets=sets,
            reps=reps,
            weight=weight
        )
        return redirect('workout_detail', pk=workout.id)
    
    return render(request, 'workouts/exercise_form.html', {'workout': workout})

#EXERCISE UPDATE VIEW 

def exercise_update(request, pk):
    exercise = get_object_or_404(Exercise, pk=pk)

    if request.method == 'POST':
        exercise.name = request.POST.get('name')
        exercise.category = request.POST.get('category')
        exercise.sets = request.POST.get('sets')
        exercise.reps = request.POST.get('reps')
        exercise.weight = request.POST.get('weight')
        exercise.save()
        return redirect('workout_detail', pk=exercise.workout.id)
    
    return render(request, 'workouts/exercise_form.html', {'exercise': exercise, 'workout': exercise.workout})

