
from django.contrib import admin
from django.urls import path, include
from workouts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Home.as_view(), name='home'),    
    path('workouts/', include('workouts.urls')),
    path('account/', include('django.contrib.auth.urls')),
    path('accocunt/signup/', views.signup, name='signup'),
   
]
