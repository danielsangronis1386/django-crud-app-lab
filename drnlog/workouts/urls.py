from django.urls import path
from . import views

urlpatterns = [
  
  path ('', views.workout_list, name='workout_list'),
  path ('new/', views.workout_create, name='workout_create'),
  path ('<int:pk>/', views.workout_detail, name='workout_detail'),
  path('<int:pk>/edit/', views.workout_update, name='workout_update'),
  path('<int:pk>/delete/', views.workout_delete, name='workout_delete'),
  path('<int:workout_id>/exercise/new/', views.exercise_create, name='exercise_create'),
  path('exercise/<int:pk>/edit/', views.exercise_update, name='exercise_update'),
  path('exercise/<int:pk>/delete/', views.exercise_delete, name='exercise_delete'),
  path('muscleparts/', views.musclepart_list, name='musclepart_list'),
  path('muscleparts/new/', views.musclepart_create, name='musclepart_create'),
  path('muscleparts/<int:pk>/', views.musclepart_detail, name='musclepart_detail'),
  path('muscleparts/<int:pk>/edit/', views.musclepart_update, name='musclepart_update'),
  path('muscleparts/<int:pk>/delete/', views.musclepart_delete, name='musclepart_delete'),

]
