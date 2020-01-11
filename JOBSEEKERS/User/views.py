from django.shortcuts import render

# Create your views here.
def User_Home_View(request):
    Temp = "User\index.html"
    return render(request, Temp)