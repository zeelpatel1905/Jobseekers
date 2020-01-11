from django.shortcuts import render

# Create your views here.

def Home_Route_View(request):
    Temp = "home_direction.html"
    return render(request, Temp)