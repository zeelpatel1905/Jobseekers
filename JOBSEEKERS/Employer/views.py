from django.shortcuts import render

# Create your views here.
def Company_Home_View(request):
    Temp = "Employer\index.html"
    return render(request, Temp)