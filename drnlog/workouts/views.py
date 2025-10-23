from django.shortcuts import render, redirect, get_object_or_404
from .models import Workout, Exercise, MusclePart


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
        muscle_parts = request.POST.getlist('muscle_parts')

        exercise = Exercise.objects.create(
            workout=workout,
            name=name,
            category=category,
            sets=sets,
            reps=reps,
            weight=weight
        )
        exercise.muscle_parts.set(muscle_parts)
        return redirect('workout_detail', pk=workout.id)
    
    from .models import MusclePart
    muscle_parts = MusclePart.objects.all()
    return render(request, 'workouts/exercise_form.html', {
        'workout': workout,
        'muscle_parts': muscle_parts
        
    })
    
#EXERCISE UPDATE VIEW 

def exercise_update(request, pk):
    exercise = get_object_or_404(Exercise, pk=pk)
    workout = exercise.workout

    if request.method == 'POST':
        exercise.name = request.POST.get('name')
        exercise.category = request.POST.get('category')
        exercise.sets = request.POST.get('sets')
        exercise.reps = request.POST.get('reps')
        exercise.weight = request.POST.get('weight')
        muscle_parts = request.POST.getlist('muscle_parts')

        exercise.save()
        exercise.muscle_parts.set(muscle_parts)
        return redirect('workout_detail', pk=exercise.workout.id)
    
    from .models import MusclePart
    muscle_parts = MusclePart.objects.all()
    return render(request, 'workouts/exercise_form.html', {
        'exercise': exercise,
        'workout': workout,
        'muscle_parts': muscle_parts

    })
    

#EXERCISE DELETE VIEW 
def exercise_delete(request, pk):
    exercise = get_object_or_404(Exercise, pk=pk)
    workout = exercise.workout

    if request.method == 'POST':
        exercise.delete()
        return redirect('workout_detail', pk=workout.id)
    
    return render(request, 'workouts/exercise_confirm_delete.html', {'exercise': exercise})

# LIST VIEW - show all muscle parts 
def musclepart_list(request):
    muscle_parts = MusclePart.objects.all()
    return render(request, 'workouts/musclepart_list.html', {'muscle_parts': muscle_parts})

# DETAIL VIEW - show one muscle part
def musclepart_detail(request, pk):
    muscle_part = get_object_or_404(MusclePart, pk=pk)
    return render(request, 'workouts/musclepart_detail.html', {'muscle_part':muscle_part})

# CREATE VIEW - add a new muscle part
def musclepart_create(request):
    if request.method =='POST':
        name = request.POST.get('name')
        MusclePart.objects.create(name=name)
        return redirect('musclepart_list')
    return render(request, 'workouts/musclepart_form.html')

# UPDATE VIEW - edit a muscle part
def musclepart_update(request,pk):
    muscle_part =get_object_or_404(MusclePart, pk=pk)
    if request.method == 'POST':
        muscle_part.name = request.POST.get('name')
        muscle_part.save()
        return redirect('musclepart_detail', pk=muscle_part.id)
    return render(request, 'workouts/musclepart_form.html', {'muscle_part': muscle_part})

# DELETE VIEW - remove a musclepart
def musclepart_delete(request, pk):
    muscle_part = get_object_or_404(MusclePart, pk=pk)
    if request.method =='POST':
        muscle_part.delete()
        return redirect('musclepart_list')
    return render(request, 'workouts/musclepart_confirm_delete.html', {'muscle_part': muscle_part})







