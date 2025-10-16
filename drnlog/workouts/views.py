from django.http import HttpResponse

def index(request):
    return HttpResponse("Welcome to your Workout Tracker!")

# Create your views here.
