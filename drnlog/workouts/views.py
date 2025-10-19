from django.shortcuts import render, redirect, get_object_or_404
from .models import Workout
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
    from .models import Category

    if request.method == 'POST':
        name = request.POST.get('name')
        duration = request.POST.get('duration')
        notes = request.POST.get('notes')
        category_id = request.POST.get('category')


        category = Category.objects.get(id=category_id)


        Workout.objects.create(
            name=name, 
            duration=duration, 
            notes=notes,
            categoy=category
        )
        return redirect('workout_list')
    # if GET send available categories tot he form 

    categories = Category.objects.all()
    return render(request, 'workouts/workout_form.html', {'categories': categories})

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
