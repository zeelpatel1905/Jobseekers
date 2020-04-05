from django.urls import path, include
from .views import User_Home_View
app_name = "Employee"

urlpatterns = [
    path('', User_Home_View, name='Home'),
    # path('accounts/',include('allauth.urls')),
]