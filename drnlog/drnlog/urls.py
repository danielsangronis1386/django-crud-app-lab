
from django.contrib import admin
from django.urls import path, include
from workouts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home.as_view(), name='home'),    
    path('workouts/', include('workouts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', views.signup, name='signup'),
   
]
