from django.urls import path
from .views import Company_Home_View
app_name = "Company"

urlpatterns = [
    path('', Company_Home_View, name='Home'),
]